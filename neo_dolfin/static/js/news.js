const newsSource = [
    {
        id: 1,
        title: "Highlighted News Title",
        excerpt: "Short description or excerpt about the highlighted news item.",
        content: "Full content of the highlighted news...",
        image: "path_to_highlighted_image.jpg"
    },
    {
        id: 2,
        title: "News  1",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },

    {
        id: 3,
        title: "Trying my luck",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },
    {
        id: 4,
        title: "Trying my luck",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },
    {
        id:5,
        title: "Trying my luck",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },
    {
        id: 6,
        title: "Trying my luck",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },
    {
        id: 7,
        title: "Trying my luck",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },
    {
        id: 8,
        title: "Trying my luck",
        excerpt: "Short description...",
        content: "Full content of the news 1...",
        image: "path_to_image_1.jpg"
    },
    
    //more news items
];

function renderNewsItems() {
    const newsContainer = document.getElementById('newsContainer');
    let newsHTML = '';

    newsSource.forEach((news, index) => {
        let columnSize = 'col-md-3';
        if (index === 0) columnSize = 'col-md-6'; // Highlighted news
        
        newsHTML += `
        <div class="${columnSize} mt-4">
            <div class="news-item">
                <div class="news-image" style="background-image: url('${news.image}');"></div>
                <div class="p-3">
                    <h4>${news.title}</h4>
                    <p>${news.excerpt}</p>
                    <a href="#" onclick="openFullNews(${news.id})" class="btn btn-primary">Read More</a>
                </div>
            </div>
        </div>
        `;
    });

    newsContainer.innerHTML = newsHTML;
}

function openFullNews(newsId) {
    window.location.href = `/newsdetails/${newsId}`;
}

function displayFullNews(newsId) {
    const newsItem = newsSource.find(item => item.id === newsId);
    if (newsItem) {
        document.getElementById('newsTitle').textContent = newsItem.title;
        document.getElementById('newsContent').textContent = newsItem.content;
        document.getElementById('newsImage').style.backgroundImage = `url('${newsItem.image}')`;
    }
}

window.onload = renderNewsItems;
