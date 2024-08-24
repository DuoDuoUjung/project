document.getElementById('toggle-btn').addEventListener('click', function () {
    var sidebar = document.getElementById('sidebar');
    var toggleBtn = document.getElementById('toggle-btn');
    var content = document.querySelector('.content');

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
