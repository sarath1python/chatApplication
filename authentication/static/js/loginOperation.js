function loginAuthentication() {
  var xhttp = new XMLHttpRequest();
  var url = "http://127.0.0.1:8080/login/user/"
  var token
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      token = this.responseText
    }
  };
  var username = document.getElementById('username').value
  var password = document.getElementById('password').value
  var params = {
    "username":username,
    "password":password
  }
  xhttp.open("POST", url, true);
  xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  xhttp.setRequestHeader('Content-Type', 'application/json');
  console.log(params)
  xhttp.send(params);
}