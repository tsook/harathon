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

	$(".delete-mark").on("click", function(e){
   		e.stopPropagation();
		if(confirm("Are you sure you want to delete this?")){
			var parent = $(this).parent().parent()
			var id = parent.data("id")
			$.ajax({
				type: "GET",
				url: 'delete',
				data: {'id': id},
	            beforeSend: function(xhr) {
	                xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}' );
	            },
	            success: function(data){
	            	location.reload()
	            }
			})
		}
	})
	$("#change-view").on("click", function(){
		if($("#change-view").data("status") == "list"){
			$("#all-debt").hide()
			$("#graph-view").show()
			$("#change-view").data("status", "graph")
		}else{
			$("#all-debt").show()
			$("#graph-view").hide()
			$("#change-view").data("status", "list")
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
