$(document).ready(function(){
	$(".add-debt").on("click", showForm);
	$(".debt-list").on("click", ".debt-entry", function(){
		var more_info = $(this).find(".more-info")
		if(more_info.data("hidden")){
			more_info.show()
			more_info.data("hidden", false)
		}else{
			more_info.hide()
			more_info.data("hidden", true)
		}
	})
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
