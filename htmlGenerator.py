import json

def json2Html(json_file):
    with open(json_file, 'r') as file:
        articles = json.load(file)
    num_objects = len(articles)

    html = f'''
     <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Quick news </title>
  <link rel="stylesheet" href="https://unpkg.com/bulma@0.9.4/css/bulma.min.css" />
  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"
    integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <link rel="stylesheet" href="../css/bulma-divider.min.css">

<link rel="stylesheet" href="static/css/style.css">
</head>

<body>
  <!-- START NAV -->
  <nav class="navbar">
    <div class="container">
        <div class="navbar-brand">
            <a class="navbar-item" href="../">
                <img style="width:100px!important;height:auto;max-height:100px;" src="static/images/logo.png" alt="Logo">
            </a>
            <span class="navbar-burger burger" data-target="navbarMenu">
                <span></span>
                <span></span>
                <span></span>
            </span>
        </div>
        <div id="navbarMenu" class="navbar-menu">
            <div class="navbar-end">
                <span class="navbar-item">
                    <a class="button" href="../" style="color: #141E46;">
                        <span class="icon">
                            <i class="fa fa-home" aria-hidden="true"></i>
                        </span>
                        <span>Home</span>
                    </a>
                </span>

            </div>
        </div>
    </div>
</nav>
  <!-- END NAV -->
<h1 class="title" style="text-align:center;">Articles {num_objects}</h1>
  <!-- Image -->
  <section class="hero ">

        
        
    '''

    for article in articles:
        html += f'''
            
            
            
            <section class="section">
          <div class="columns">
            <div class="column is-8 is-offset-2">
              <div class="content is-medium">
                
                <h2 class="title"><a href="{article['Url']}">{article['Title']}</a></h2>
                <span class="link">--{article['Source']}</span>
                <h3 class="subtitle is-4" onclick="toggleExpand(this)">{article['Summary']}</h3>
                <p class="element-article">{article['Content']}</p></div></div>
              </div>
            </div>
          </div>
        </section>

        <div class="is-divider"></div>
        '''

    html += '''
       </div>
    </div>
  </section>


  <script>
    document.addEventListener('DOMContentLoaded', () => {

      // Get all "navbar-burger" elements
      const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

      // Check if there are any navbar burgers
      if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
          el.addEventListener('click', () => {

            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle('is-active');
            $target.classList.toggle('is-active');

          });
        });
      }

    });
    
       // JavaScript to toggle the 'expanded' class on click
            function toggleExpand(element) {
                var articleElement = element.nextElementSibling;
                articleElement.classList.toggle("expanded");
            }
  </script>

</body>

</html>
    '''

    return html
