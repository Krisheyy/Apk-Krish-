from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html>
<head>
<title>Krish Server</title>
<style>
body {
  font-family: sans-serif; /* Use a modern font */
  margin: 0; /* Remove default margins */
  background-color: #f0f0f0; /* Light background */
}.container {
  max-width: 960px; /* Set a maximum width */
  margin: 0 auto; /* Center the content */
  padding: 20px;
}.header {
  text-align: center; /* Center the header text */
  margin-bottom: 20px;
}.image-container {
  width: 100%; /* Make image responsive */
  text-align: center; /* Center the image */
}.main-image {
  max-width: 100%; /* Ensure image scales down */
  height: auto; /* Maintain aspect ratio */
  display: block; /* Prevent image from creating space below */
}.offerings {
  display: grid; /* Use grid layout */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); /* Responsive columns */
  grid-gap: 20px; /* Spacing between grid items */
  margin-top: 20px;
}.offering {
  border: 1px solid #ccc; /* Add a border */
  padding: 20px;
  text-align: center; /* Center the content */
}.offering img {
  max-width: 100px; /* Limit icon size */
  margin-bottom: 10px;
}.button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50; /* Green button */
  color: white;
  text-decoration: none;
  border-radius: 5px;
}.bottom-section {
  margin-top: 20px;
  text-align: center; /* Center the content */
}.ping-datetime {
  font-size: 14px;
  color: #777; /* Gray color */
}
</style>
</head>
<body>

<div class="container">
  <div class="header">
    <h1>KRISH SERVER</h1>
  </div>

  <div class="image-container">
    <img class="main-image" src="https://i.ibb.co/cpDK2Cr/20250214-130623.jpg" alt=""> </div>

  <div class="offerings">
    <div class="offering">
      <img src="https://i.ibb.co/zhWc8BhC/20250214-124000.jpg" alt="Convo Icon">
      <h2>CONVO</h2>
      <a href="https://convo-gm5o.onrender.com" class="button">View</a>
    </div>
    <div class="offering">
      <img src="https://i.ibb.co/CK5hsy4p/20250214-124055.jpg" alt="">
      <h2>GROUP TID</h2>
      <a href="http://65.108.3.108:22372/" class="button">View</a>
    </div>
    <div class="offering">
      <img src="https://i.ibb.co/LDvJRpM6/20250214-124143.jpg" alt="Pricing Icon">
      <h2>TOKEN CHEAKER</h2>
      <a href="https://tokens.darkeagle.online/" class="button">View</a>
    </div>
    <div class="offering">
      <img src="https://i.ibb.co/ksrMh7nd/20250214-125419.jpg" alt="Status Icon">
      <h2>COMMENT</h2>
      <a href="www." class="button">View</a>
    </div>
  </div>

  <div class="bottom-section">
    <div class="ping-datetime">
      Ping: <span id="ping">Calculating...</span> | Date & Time: <span id="datetime"></span>
    </div>
    <p>&copy; 2025 Krish Era All Rights Reserved.</p>
    <p>Made with &hearts; by Abhi X Krish</p>
  </div>
</div>

<script>
// Simulate ping (replace with actual ping calculation)
setTimeout(() => {
  document.getElementById('ping').textContent = '25ms';
}, 1000); // Update every second

// Update date and time
function updateDateTime() {
  const now = new Date();
  const formattedDateTime = now.toLocaleString();
  document.getElementById('datetime').textContent = formattedDateTime;
}

updateDateTime(); // Initial call
setInterval(updateDateTime, 1000); // Update every second
</script>

</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
