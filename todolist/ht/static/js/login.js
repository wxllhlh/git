$(document).ready(function(request)
{
	jQuery(document).ajaxSend(function(event, xhr, settings) {
	    function getCookie(name) {
	        var cookieValue = null;
	        if (document.cookie && document.cookie != '') {
	            var cookies = document.cookie.split(';');
	            for (var i = 0; i < cookies.length; i++) {
	                var cookie = jQuery.trim(cookies[i]);
	                // Does this cookie string begin with the name we want?
	                if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                    break;
	                }
	            }
	        }
	        return cookieValue;
	    }
	    function sameOrigin(url) {
	        // url could be relative or scheme relative or absolute
	        var host = document.location.host; // host + port
	        var protocol = document.location.protocol;
	        var sr_origin = '//' + host;
	        var origin = protocol + sr_origin;
	        // Allow absolute or scheme relative URLs to same origin
	        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
	            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
	            // or any other URL that isn't scheme relative or absolute i.e relative.
	            !(/^(\/\/|http:|https:).*/.test(url));
	    }
	    function safeMethod(method) {
	        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	    }
	 
	    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
	        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	    }
	});
	if(a==1)
	{
		$("#login").hide();
		$("#login_name").show();
		ShowList();
		
	}
	else
	{
		$("#login").show();
		$("#login_name").hide();
	}
});
function ShowList()
{
	$("#Todolist").empty();
	$("#Donelist").empty();
	$.post("../list.json/",function(data){
		for(var i in data)
		{
			if(data[i].status == 0)
			{
				$("#Todolist").append("<div id='" +data[i].id + "' > </div>");
				$("#Todolist").children("#"+data[i].id).append("<h3>"+data[i].title+
				"<button type=\"button\" onclick=\"ToDoChangeToDone(this)\" class=\"btn btn-default btn-info todolist\" > 完成</button> "+
				" <button type=\"button\" onclick=\"DeleteThing(this)\" class=\"btn btn-default btn-info todolist\" style=\"background: #f16a6a\">删除</button> </h3>"+
				"<div id='show"+data[i].id+"'  style=\"display:none\" > <p>"+data[i].description+"</p>"+
				"<p><a onclick=\"hidedetail(this)\"class=\"btn\">View details «</a></p></div>"+
				"<div id='hide"+data[i].id+"'><p><a onclick=\"showdetail(this)\"class=\"btn\">View details »</a></p></div>");
			}
			else
			{
				$("#Donelist").append("<div id='" +data[i].id + "' > </div>");
				$("#Donelist").children("#"+data[i].id).append("<h3>"+data[i].title+
				"<button type=\"button\" onclick=\"DoneChangeToTodo(this)\" class=\"btn btn-default btn-info todolist\" style=\"background: #f9c35d\"> 未完成</button>"+
				"<button type=\"button\" onclick=\"DeleteThing(this)\" class=\"btn btn-default btn-info todolist\" style=\"background: #f16a6a\">删除</button> </h3>"+
				"<div id='show"+data[i].id+"'  style=\"display:none\" > <p>"+data[i].description+"</p>"+
				"<p><a onclick=\"hidedetail(this)\"class=\"btn\">View details «</a></p></div>"+
				"<div id='hide"+data[i].id+"'><p><a onclick=\"showdetail(this)\"class=\"btn\">View details »</a></p></div>");
			}
		}
	})
	
}
function showdetail(obj)
{
	$(obj).parent().parent().prev().show("slow");
	$(obj).parent().parent().hide("slow");
}
function hidedetail(obj)
{
	$(obj).parent().parent().next().show("slow")
	$(obj).parent().parent().hide("slow")
}

function trim(str)
{
	str = str.replace(/^ +/,'');
	str = str.replace(/ +$/,'');
	return str;
} 

function checktitle()
{
	var text = $("$title").val();
	alert("!");
	if(text=="")
	{
		alert('user is null');
	}
	return false;
}

function ToDoChangeToDone(obj)
{
	var id = $(obj).parent().parent().attr("id");
	$.post("../change/",{id:id,status:1},function(data){
		ShowList();
	})
}

function DoneChangeToTodo(obj)
{
	var id = $(obj).parent().parent().attr("id");
	$.post("../change/",{id:id,status:0},function(data){
		ShowList();
	})
}
function DeleteThing(obj)
{
	var id = $(obj).parent().parent().attr("id");
	$.post("../delete/",{id:id},function(data){
		ShowList();
	})
}


function sleep(numberMillis) 
{ 
   var now = new Date();
   var exitTime = now.getTime() + numberMillis;  
   while(true) 
   	{ 
       	now = new Date(); 
       	if(now.getTime() > exitTime)
       	return;
    }

}