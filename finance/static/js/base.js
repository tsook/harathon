$(document).ready(function() {
    $("#about").on("click", function(){
    	$(".popup").css("display", "block")
    })
    $("#close-about").on("click", function(){
    	$(".popup").css("display", "none")
    })
});