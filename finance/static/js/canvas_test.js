var dis = 150
var radius = 20
var number = 7

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d")

function makeLine(from, to){
	var fromAngle = 2*Math.PI/number * from
	var toAngle = 2*Math.PI/number * to
	ctx.moveTo(dis*Math.cos(fromAngle) + 250, dis*Math.sin(fromAngle) + 250)
	ctx.lineTo(dis*Math.cos(toAngle) + 250, dis*Math.sin(toAngle) + 250)
	ctx.stroke();
}

makeLine(1, 2)
makeLine(6, 4)

for(var i = 0; i <= 2*Math.PI; i += 2*Math.PI/number){
	ctx.beginPath()
	ctx.arc(dis*Math.cos(i) + 250, dis*Math.sin(i) + 250, radius, 0, 2*Math.PI)
	ctx.fillStyle = "white"
	ctx.fill()
	ctx.stroke()
	ctx.fillStyle= "black"
	ctx.font = "30px Arial";
	ctx.fillText(i/(2*Math.PI/number), dis*Math.cos(i) + 240, dis*Math.sin(i) + 260);
}