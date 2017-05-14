var dis = 300
var radius = 40
var nodes = [];
var edges = [];

$.ajax({
	type: "GET",
	url: '/get_list/',
	dataType: 'json',
	data: {'name': name},
	beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}' );
    },
    success: function(data){
    	console.log(data)
    	for(var entry in data){
    		console.log(entry)
    		console.log(entry.fields)
    		if(!nodes.includes(entry.fields.giver))
    			nodes.push(entry.fields.giver)
    		if(!nodes.includes(entry.fields.receiver))
    			nodes.push(entry.fields.receiver)
    		if(!edges.includes(entry.fields.receiver + "-" + entry.fields.giver))
    			edges.push(entry.fields.receiver+"-"+entry.fields.giver)
    	}
    }
})

$(document).ready(function(){
	for(edge in edges){
		edge = edge.split("-")
		var from = edge[0]
		var to = edge[1]
		makeLine(nodes.indexOf(from), nodes.indexOf(to))
	}
	makeCircles(nodes)
})

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d")

function makeLine(from, to){
	var fromAngle = 2*Math.PI/number * from
	var toAngle = 2*Math.PI/number * to
	ctx.moveTo(dis*Math.cos(fromAngle) + 400, dis*Math.sin(fromAngle) + 400)
	ctx.lineTo(dis*Math.cos(toAngle) + 400, dis*Math.sin(toAngle) + 400)
	ctx.lineWidth = 5;
	ctx.strokeStyle = "#244e3b"
	ctx.stroke();
}

function makeCircles(nodes){
	for(var i = 0; i < nodes.length; i++){
		var angle = i * 2*Math.PI/nodes.length
		ctx.strokeStyle = "#326b51"
		ctx.beginPath()
		ctx.arc(dis*Math.cos(angle) + 400, dis*Math.sin(angle) + 400, radius, 0, 2*Math.PI)
		ctx.fillStyle = "#9cd4ba"
		ctx.fill()
		ctx.stroke()
		ctx.fillStyle= "#326b51"
		ctx.font = "30px Verdana";
		ctx.fillText(nodes[i][0], dis*Math.cos(angle) + 380, dis*Math.sin(angle) + 410);
	}	
}


