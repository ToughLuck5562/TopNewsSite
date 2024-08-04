
async function GetTopNews() {

    function CreateCard(title, link) {

        const card = document.createElement('div');
        card.className = 'container-news';

        const h2 = document.createElement('h2');
        h2.textContent = title;

        const button = document.createElement('button');
        button.className = 'button';
        button.textContent = 'View More';
        button.onclick = function() {
            window.location.href = link;
        };

        card.appendChild(h2);
        card.appendChild(button);

        document.getElementById('container-top-news-ul').appendChild(card);
    }

    try {

        const TopNewsAPI = await fetch('/get_top_news');
        const TopNewsAPIData = await TopNewsAPI.json();

        TopNewsAPIData.forEach(element => {
            CreateCard(element['ArticleHeadline'], element['ArticleLink'])
        });

    } catch(error) {
        console.log(error)
    }

};

GetTopNews()