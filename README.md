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
<p><i>Сonducts 5 smok tests with different users. First user - correct user.Users 2 - 5 have problems.</i></p>

<h3>Test - 1. Conducts smoke-testing:</h3>
<ol>
  <li>Correct login.</li>
  <li>Chose product.</li>
  <li>Add product to cart.</li>
  <li>Put ingo about order.</li>
  <li>Confirms his order.</li>
</ol>

<h3>Test - 2. Blocked user - no have access to system:</h3>
<ol>
  <li>Put login and password, click button "login".</li>
  <li>Make screenshots, because user on have access to system.</li>
</ol>

<h3>Test - 3. Problem user - have problem with work system:</h3>
<ol>
  <li>Correct login.</li>
  <li>Chose product.</li>
  <li>Add product to cart.</li>
  <li>Put ingo about order.</li>
  <li>Confirms his order.</li>
  <li>Makes screens on all steps.</li>
</ol>

<h3>Test - 4. Error user - have problem with work system not in all steps:</h3>
<ol>
  <li>Correct login.</li>
  <li>Chose product.</li>
  <li>Add product to cart.</li>
  <li>Put ingo about order.</li>
  <li>Confirms his order.</li>
  <li>Makes screens on all steps.</li>
</ol>

<h3>Test - 5. Visual user - has a problem displaying elements:</h3>
<ol>
  <li>Correct login.</li>
  <li>Chose product.</li>
  <li>Add product to cart.</li>
  <li>Put ingo about order.</li>
  <li>Confirms his order.</li>
  <li>Makes screens on all steps.</li>
</ol>
