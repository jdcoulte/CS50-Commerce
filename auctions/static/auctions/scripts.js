
console.log(window.location.href);

var getParams = function (url) {
	var params = {};
	var parser = document.createElement('a');
	parser.href = url;
	var query = parser.search.substring(1);
	var vars = query.split('&');
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	return params;
};

var RedirectParams = function(url) {
    
    var params = getParams(url);
    
    if(params.length == 0) {
        return false;
    }
    else {
        document.querySelector("#redirectinput").value = params.next;
        return true;
    }
};