function run() {
  let main_parent = document.getElementById("chat-tab").parentNode;

  main_parent.childNodes[0].classList.add("header-bar");
  main_parent.style = "padding: 0; margin: 0";
  main_parent.parentNode.style = "gap: 0";
  main_parent.parentNode.parentNode.style = "padding: 0";

  // const version_node = document.createElement("p");
  // version_node.innerHTML = "version: KH_APP_VERSION";
  // version_node.style = "position: fixed; top: 10px; right: 10px;";
  // version_node.innerHTML = `<img src="https://i.ibb.co/p0M3R93/logo.png" alt="black12" style="width: 180px; height: 110px; vertical-align: middle; margin-right: 5px;">`;
  // version_node.innerHTML = <img src="https://i.ibb.co/p0M3R93/logo.png" alt="logo" border="0"></img>
  // version_node.style.overflow = "visible";
  // version_node.innerHTML = "Version:1.0";
  // version_node.style = "position: fixed; top: 0px; right: 10px;";
  // main_parent.appendChild(version_node);
  // 创建并添加 logo 图片
  // 创建版本信息和 logo 图片的 HTML
  const version_node = document.createElement("div");

  version_node.style.position = "fixed"; // 固定位置
  version_node.style.top = "10px"; // 距离顶部10px
  version_node.style.right = "10px"; // 距离右侧10px
  version_node.style.zIndex = "1000"; // 确保在其他元素之上
  version_node.innerHTML = `<img src="https://i.ibb.co/5Y1CSnP/black12.png" alt="black12" style="width: 180px; height: 110px; vertical-align: middle; margin-right: 5px;">`;
  // version_node.innerHTML = `<img src="https://i.ibb.co/HN2W3tT/logo-new.png" alt="black12" style=" vertical-align: middle; margin-right: 5px;">`;

  // version_node.innerHTML = `<img src="file:///home/dshengq/github/kotaemon/libs/ktem/ktem/assets/img/logo.png" alt="Logo" style="width: 180px; height: 90px;vertical-align: middle; margin-right: 5px;">`;
  // version_node.innerHTML = `<img src="https://i.ibb.co/HN2W3tT/logo-new.png" alt="Logo" style="width: 180px; height: 90px;">`;


  main_parent.appendChild(version_node); // 将版本信息和 logo 添加到父元素

  // clpse
  globalThis.clpseFn = (id) => {
    var obj = document.getElementById('clpse-btn-' + id);
    obj.classList.toggle("clpse-active");
    var content = obj.nextElementSibling;
    if (content.style.display === "none") {
      content.style.display = "block";
    } else {
      content.style.display = "none";
    }
  }

  // store info in local storage
  globalThis.setStorage = (key, value) => {
      localStorage.setItem(key, value)
  }
  globalThis.getStorage = (key, value) => {
    item = localStorage.getItem(key);
    return item ? item : value;
  }
  globalThis.removeFromStorage = (key) => {
      localStorage.removeItem(key)
  }
}
