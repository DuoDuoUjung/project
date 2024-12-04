document.getElementById('toggle-btn').addEventListener('click', function () {
    var sidebar = document.getElementById('sidebar');
    var toggleBtn = document.getElementById('toggle-btn');
    var content = document.querySelector('.content');

    // 切换侧边栏的收起/展开状态
    sidebar.classList.toggle('sidebar-collapsed');
    toggleBtn.classList.toggle('toggle-btn-collapsed');
    content.classList.toggle('content-expanded');

    // 切换箭头方向
    if (toggleBtn.classList.contains('toggle-btn-collapsed')) {
        toggleBtn.innerHTML = '&#9654;'; // 向右箭头
    } else {
        toggleBtn.innerHTML = '&#9664;'; // 向左箭头
    }
});

// 设置 toggle-btn 的高度为 sidebar 的高度
function adjustToggleBtnHeight() {
    var sidebar = document.getElementById('sidebar');
    var toggleBtn = document.getElementById('toggle-btn');
    if (sidebar && toggleBtn) {
        toggleBtn.style.height = sidebar.offsetHeight + 'px';
    }
}

// 初始化时调整按钮高度
document.addEventListener('DOMContentLoaded', adjustToggleBtnHeight);

// 窗口调整大小时同步按钮高度
window.addEventListener('resize', adjustToggleBtnHeight);