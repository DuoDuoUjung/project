document.addEventListener("DOMContentLoaded", function () {
    // 初始化頁面
    initializePage();

    // 綁定課程選單的下拉功能
    const courseSelect = document.getElementById('course-select');
    if (courseSelect) {
        courseSelect.addEventListener('click', toggleDropdown);
    }

    // 點擊頁面其他地方隱藏下拉選單
    document.addEventListener('click', function (e) {
        const dropdownOptions = document.getElementById('dropdown-options');
        if (!e.target.closest('.course-header') && dropdownOptions.style.display === 'block') {
            dropdownOptions.style.display = 'none';
            console.log("Dropdown closed by clicking outside");
        }
    });

    // 綁定好友操作
    document.querySelectorAll('.friends-list li').forEach(item => {
        const avatar = item.querySelector('.friend-avatar');
        const leftSide = item.querySelector('.left-side');
        const rightSide = item.querySelector('.right-side');
        const friendNameElement = item.querySelector('.friend-name');

        // 綁定頭像點擊
        if (avatar) {
            avatar.addEventListener('click', (e) => {
                e.stopPropagation();
                handleFriendSelection(item, friendNameElement, "profile");
            });
        }

        // 綁定左側點擊
        if (leftSide) {
            leftSide.addEventListener('click', () => {
                handleFriendSelection(item, friendNameElement, "profile");
            });
        }

        // 綁定右側點擊
        if (rightSide) {
            rightSide.addEventListener('click', () => {
                handleFriendSelection(item, friendNameElement, "chat");
            });
        }
    });

    /**
     * 初始化頁面：隱藏區域並加載課程數據
     */
    function initializePage() {
        console.log("Initializing page...");
        const chatArea = document.getElementById('chat-area');
        const profileInfo = document.getElementById('profile-info');
        if (chatArea) chatArea.style.display = 'none';
        if (profileInfo) profileInfo.style.display = 'none';

        // 初始加載課程數據
        loadCourses();

        // 創建顯示選中課程的區域
        const courseSelectionArea = document.createElement('div');
        courseSelectionArea.id = "selected-course";
        courseSelectionArea.innerHTML = "<strong>尚未選擇課程</strong>";
        document.querySelector('.course-menu').appendChild(courseSelectionArea);

        console.log("Page initialized");
    }

    /**
     * 根據點擊類型處理好友選擇
     * @param {HTMLElement} friendItem - 好友列表項目
     * @param {HTMLElement} friendNameElement - 好友名稱元素
     * @param {string} actionType - 點擊類型 ("profile" 或 "chat")
     */
    function handleFriendSelection(friendItem, friendNameElement, actionType) {
        const friendName = friendNameElement.textContent.trim();
        selectFriend(friendItem);

        if (actionType === "profile") {
            showProfileInfo(friendName, friendItem);
        } else if (actionType === "chat") {
            showChat(friendName);
        }
    }

    /**
     * 設置選中好友的樣式
     * @param {HTMLElement} friendItem - 好友列表項目
     */
    function selectFriend(friendItem) {
        document.querySelectorAll('.friends-list li').forEach(item => {
            item.classList.remove('selected');
        });
        friendItem.classList.add('selected');
    }

    /**
     * 顯示好友個人資料
     * @param {string} friendName - 好友名稱
     * @param {HTMLElement} friendItem - 好友列表項目
     */
    function showProfileInfo(friendName, friendItem) {
        const profileInfo = document.getElementById('profile-info');
        const chatArea = document.getElementById('chat-area');
        const profileNameElement = document.getElementById('profile-name');
        const profileAvatarElement = document.getElementById('profile-avatar');

        if (profileInfo && chatArea) {
            profileInfo.style.display = 'flex';
            chatArea.style.display = 'none';
        }

        if (profileNameElement) {
            profileNameElement.innerText = `姓名: ${friendName}`;
        }

        if (profileAvatarElement) {
            const friendAvatarUrl = friendItem.querySelector('.friend-avatar').src;
            profileAvatarElement.src = friendAvatarUrl || '/static/images/default-avatar.png';
        }
    }

    /**
     * 顯示聊天區域
     * @param {string} username - 聊天對象名稱
     */
    function showChat(username) {
        const profileInfo = document.getElementById('profile-info');
        const chatArea = document.getElementById('chat-area');
        const chatWithName = document.getElementById('chat-with-name');

        if (profileInfo && chatArea) {
            chatArea.style.display = 'flex';
            profileInfo.style.display = 'none';

            if (chatWithName) {
                chatWithName.innerText = `與 ${username} 的聊天`;
            }
        }
    }

    /**
     * 切換課程選單的顯示/隱藏
     */
    let dropdownVisible = false;

    function toggleDropdown() {
        const dropdownOptions = document.getElementById('dropdown-options');
        dropdownOptions.style.display = dropdownVisible ? 'none' : 'block';
        dropdownVisible = !dropdownVisible;
        console.log(`Dropdown visibility: ${dropdownOptions.style.display}`);
    }

    /**
     * 加載課程數據
     */
    function loadCourses() {
        console.log("Loading courses...");
        const staticCourses = [
            {
                id: 1,
                title: 'Python',
                subCourses: [
                    { name: 'Python 基礎', progress: 50 },
                    { name: 'Python 進階', progress: 30 },
                    { name: 'Python 數據分析', progress: 70 }
                ]
            },
            {
                id: 2,
                title: 'JAVA',
                subCourses: [
                    { name: 'JAVA 基礎', progress: 60 },
                    { name: 'JAVA Web 開發', progress: 40 },
                    { name: 'JAVA 框架', progress: 20 }
                ]
            },
            {
                id: 3,
                title: 'HTML',
                subCourses: [
                    { name: 'HTML 基礎', progress: 80 },
                    { name: 'HTML5 新特性', progress: 50 },
                    { name: 'HTML + CSS 設計', progress: 90 }
                ]
            },
            {
                id: 4,
                title: 'C++',
                subCourses: [
                    { name: 'C++ 基礎', progress: 40 },
                    { name: 'C++ STL', progress: 60 },
                    { name: 'C++ 高性能編程', progress: 30 }
                ]
            }
        ];
        

        populateDropdownOptions(staticCourses);
    }
    /**
     * 將課程數據填充到下拉選單中
     * @param {Array} courses - 課程數據列表
     */
    function populateDropdownOptions(courses) {
        console.log("Populating dropdown options...", courses);
        const dropdownOptions = document.getElementById('dropdown-options');
        dropdownOptions.innerHTML = ''; // 清空舊的選項

        courses.forEach(course => {
            const option = document.createElement('div');
            option.className = 'dropdown-option';
            option.textContent = course.title;
            option.addEventListener('click', function () {
                handleCourseSelection(course);
            });
            dropdownOptions.appendChild(option);
        });
    }

    

    /**
     * 處理課程選擇
     * @param {string} courseTitle - 選中的課程名稱
     */
    function handleCourseSelection(courseTitle) {
        console.log(`Course selected: ${courseTitle}`);
        const dropdownOptions = document.getElementById('dropdown-options');
        const selectedCourse = document.getElementById('selected-course');

        // 隱藏下拉選單
        dropdownOptions.style.display = 'none';
        dropdownVisible = false;

        // 更新選中課程顯示區域
        selectedCourse.innerHTML = `<strong>你選擇了:</strong> ${courseTitle}`;
    }

    /**
     * 處理課程選擇
     * @param {Object} course - 選中的課程對象
     */
     function handleCourseSelection(course) {
        console.log(`Course selected: ${course.title}`);
    const dropdownOptions = document.getElementById('dropdown-options');
    const selectedCourse = document.getElementById('selected-course');

        // 隱藏下拉選單
        dropdownOptions.style.display = 'none';
        dropdownVisible = false;

        fetchCourseProgress(course.id)
        .then(progressData => {
            // 生成課程進度條
            // 生成進度條的 HTML
const subCourseList = progressData.subCourses
.map(subCourse => `
    <div class="course-progress">
        <span>${subCourse.name}</span>
        <div class="progress-bar">
            <div class="progress" style="width: ${subCourse.progress}%;"></div>
        </div>
    </div>
`)
.join('');


            selectedCourse.innerHTML = `
                <h3>${course.title} 的課程進度</h3>
                ${subCourseList}
            `;
            selectedCourse.style.display = 'block';
        })
        .catch(error => {
            console.error("Error fetching course progress:", error);
            selectedCourse.innerHTML = `<strong>無法加載課程進度，請稍後再試。</strong>`;
            selectedCourse.style.display = 'block';
        });
}

/**
 * 模擬動態數據獲取
 * @param {number} courseId - 課程 ID
 * @returns {Promise<Object>} 返回課程進度數據
 */
 function fetchCourseProgress(courseId) {
    return new Promise((resolve, reject) => {
        console.log(`Fetching progress for course ID: ${courseId}`);
        // 模擬從資料庫獲取數據
        const dynamicData = {
            1: { subCourses: [{ name: 'Python 基礎', progress: 50 }, { name: 'Python 進階', progress: 30 }, { name: 'Python 數據分析', progress: 70 }] },
            2: { subCourses: [{ name: 'JAVA 基礎', progress: 60 }, { name: 'JAVA Web 開發', progress: 40 }, { name: 'JAVA 框架', progress: 20 }] },
            3: { subCourses: [{ name: 'HTML 基礎', progress: 80 }, { name: 'HTML5 新特性', progress: 50 }, { name: 'HTML + CSS 設計', progress: 90 }] },
            4: { subCourses: [{ name: 'C++ 基礎', progress: 40 }, { name: 'C++ STL', progress: 60 }, { name: 'C++ 高性能編程', progress: 30 }] }
        };

        setTimeout(() => {
            if (dynamicData[courseId]) {
                resolve(dynamicData[courseId]);
            } else {
                reject("Course not found");
            }
        }, 500); // 模擬網絡延遲
    });
}
});
