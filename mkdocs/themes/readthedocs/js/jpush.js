$(document).ready(function(){
$("ul.subnav li span").click(function(){
    $(this).parents().siblings().css("display","block");
    var url = $(this).parents().next().children().attr("href");
    window.location.href=url;
});

$("ul.subnav li a").click(function(){
    $(this).parents().siblings().css("display","block");
});

$("[href='./']").parents().css("display","block");
$("[href='./']").parents().siblings().css("display","block");
});