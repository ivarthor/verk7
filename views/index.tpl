<!DOCTYPE html>
<html>
<style>
	body {
          background-color: lightblue;
          margin: 3em;
      }

      h3 {
          color: darkblue;
      }

      form {
          font-family: sans-serif;
      }
      input {
        padding: .3em;
        margin: .3em 1em;
      }
</style>
<head>
	<title>Verkefni 7</title>
</head>
<body>
	<h3>Nýskráning:</h3>
	<form method="post" action="/donyskra" accept-charset="ISO-8859-1" id="ny">
		Notendanaf:<br>
		<input type="text" name="user" required><br>
		Lykilorð:<br>
		<input type="text" name="pass" required><br>
		Nafn:<br>
		<input type="text" name="nafn" required><br>
		<input type="submit" value="Nýskrá">
		<input type="reset" name="Hreinsa">
	</form>
	<hr>
	<h3>Innskráningarform:</h3>
	<form method="post" action="/doinnskra" accept-charset="ISO-8859-1" id="inn">
		Notendanafn:<br>
		<input type="text" name="user" required>
		Lykilorð:<br>
		<input type="text" name="pass" required>
		<input type="submit" name="Skrá-inn">
	</form>
</body>
</html>