<!DOCTYPE html>
<html>
<style>
	body {
		background-color: beige;
		margin: 3em;
	}
	h2 {
		color: #a00;
		font-family: sans-serif;
	}
</style>
<head>
	<title>Members</title>
</head>
<body>
	<h2>Félagskrá</h2>
	<p>The member teams are as follows:</p>
	<table border="1">
		%for row in rows:
		<tr>
			%for col in row:
			<td>{{col}}</td>
			%end
		</tr>
		%end
	</table>
	<a href="/">Aftur á skráningarsíðu</a>
</body>
</html>