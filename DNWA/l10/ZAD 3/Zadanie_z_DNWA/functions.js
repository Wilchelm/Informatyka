function myFunction(MyForm) {
	var value1=document.getElementById("username").value;
	var value2=document.getElementById("password").value;
	var queryString = "?username=" + value1 + "&password=" + value2;
	window.location.href = "Zadanie_z_DNWA2.html" + queryString;
	return false;
}
function create() {
	var queryString = decodeURIComponent(window.location.search);
	queryString = queryString.substring(1);
	var queries = queryString.split("&");
	for (var i = 0; i < queries.length; i++)
	{
  		document.write("<h2><b>" + queries[i] + "</b></h2>");
	}
}
