<h1>To run the this test.</h1>
<ul>
  <li>Download the repository.</li>
  <li>Extract it.</li>
  <li>Add the project to your IDE (I recommend PyCharm).</li>
  <li>Install Pytest using the command in your IDE's terminal: "pip install pytest".</li>
  <li>Install Selenium: "pip install selenium".</li>
  <li>Install plugin pytest-ordering еo run tests in sequence: "pip install pytest-ordering".</li>
  <li>In file base.py in method "get_screenshot" change path to directory for saves screnshots on your path.</li>
  <li>While in the project directory, enter the command, for start test with info in console: "python -m pytest -s -v" or "pytest -s -v".</li>
</ul>

<h1>What does this test do.</h1>
<p>Сonducts 5 smok tests with different users. First user - correct user.Users 2 - 5 have problems.</p>
<h3>Test - 1. Conducts smoke-testing:</h3>
<ol>
  <li>Correct login.</li>
  <li>Chose product.</li>
  <li>Add product to cart.</li>
  <li>Put ingo about order.</li>
  <li>Confirms his order.</li>
</ol>
<h3>Test - 2. Blocked user:</h3>
<ol>
  <li>Put login and password, click button "login".</li>
  <li>Put login and password.</li>
</ol>
  <li></li>
  <li></li>

