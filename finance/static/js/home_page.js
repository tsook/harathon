$(document).ready(function(){
	$(".add-debt").on("click", showForm);
})

function showForm(){
	$(".add-debt-form").show()
	$(".add-debt").removeClass("btn-success")
	$(".add-debt").html("Hide")
	$(".add-debt").off("click")
	$(".add-debt").on("click", hideForm)
}

function hideForm(){
	$(".add-debt-form").hide()
	$(".add-debt").addClass("btn-success")
	$(".add-debt").html("Add New Debt")
	$(".add-debt").off("click")
	$(".add-debt").on("click", showForm)
}