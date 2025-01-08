from __future__ import annotations

from typing import Optional

import requests

from kotaemon.base import Document, Param

from .base import BaseReranking

session = requests.session()


class TeiFastReranking(BaseReranking):
    """Text Embeddings Inference (TEI) Reranking model
    (https://huggingface.co/docs/text-embeddings-inference/en/index)
    """

    endpoint_url: str = Param(
        None, help="TEI Reranking service api base URL", required=True
        # 'http://localhost:8080/rerank', help="TEI Reranking service api base URL", required=True

    )
    model_name: Optional[str] = Param(
        None,
        # "BAAI/bge-reranker-large",
        help=(
            "ID of the model to use. You can go to [Supported Models]"
            "(https://github.com/huggingface"
            "/text-embeddings-inference?tab=readme-ov-file"
            "#supported-models) to see the supported models"
        ),
    )
    is_truncated: Optional[bool] = Param(True, help="Whether to truncate the inputs")

    def client(self, query, texts):
        response = session.post(
            url=self.endpoint_url,
            json={
                "query": query,
                "texts": texts,
                # "is_truncated": self.is_truncated,  # default is True
                "is_truncated": True,  # default is True
            },
        ).json()
        return response

    def split_docs(self,docs: list[str], max_length: int = 512) -> list[str]:
        """将每个字符串切分为不超过 max_length 的部分"""
        split_list = []
        for doc in docs:
            # 检查字符串长度并切分
            while len(doc) > max_length:
                split_list.append(doc[:max_length])  # 添加前 512 字符
                doc = doc[max_length:]  # 剩余部分继续处理
            if doc:  # 添加剩余部分
                split_list.append(doc)
        return split_list


    def run(self, documents: list[Document], query: str) -> list[Document]:
        """Use the deployed TEI rerankings service to re-order documents
        with their relevance score"""
        if not self.endpoint_url:
            print("TEI API reranking URL not found. Skipping rerankings.")
            return documents

        compressed_docs: list[Document] = []

        if not documents:  # to avoid empty api call
            return compressed_docs

        if isinstance(documents[0], str):
            documents = self.prepare_input(documents)

        # batch_size = 6
        # num_batch = max(len(documents) // batch_size, 1)
        # 计算最大 batch_size，使得 num_batch 不超过 32
        total_documents = len(documents)
        max_num_batch = 32
        max_batch_size = (total_documents + max_num_batch - 1) // max_num_batch  # 向上取整

        # 最终的 batch_size 取 max_batch_size 和 32 之间的最小值
        batch_size = min(max_batch_size, 32)

        num_batch = (total_documents + batch_size - 1) // batch_size  # 向上取整

        print("num_batch,batch_size",num_batch,batch_size)

        for i in range(num_batch):
            if i == num_batch - 1:
                mini_batch = documents[batch_size * i :]
            else:
                mini_batch = documents[batch_size * i : batch_size * (i + 1)]
            
            # mini_batch = mini_batch[:32]  

            _docs = [d.content for d in mini_batch]
            _docs = self.split_docs(_docs)

            _docs = _docs[:32]

            # 检查 _docs 里每个元素的长度
            for i, doc in enumerate(_docs):
                print(f"Document {i} length: {len(doc)}")


            rerank_resp = self.client(query, _docs)
            print(f"rerank_resp: {rerank_resp}")

            # 记录原始文档的索引
            original_indices = []
            for doc in mini_batch:
                # 计算切分后的部分数量并记录原始索引
                num_parts = (len(doc.content) + 511) // 512  # 向上取整
                original_indices.extend([doc] * num_parts)

            for r in rerank_resp:
                # print("type r", type(r))
                # print("r index ", int(r["index"]))
                # 使用切分后的索引来获取原始文档
                original_doc = original_indices[int(r["index"])]
                original_doc.metadata["reranking_score"] = r["score"]
                compressed_docs.append(original_doc)

        compressed_docs = sorted(
            compressed_docs, key=lambda x: x.metadata["reranking_score"], reverse=True
        )
        return compressed_docs
