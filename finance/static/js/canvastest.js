var dis = 300
var radius = 40
var number = 10

var names = ["HK", "TK", "BA", "SH", "WK", "AS", "TS", "AS", "DB", "SA", "AB", "CA", "ZZ"]

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

makeLine(1, 2)
makeLine(5, 4)
makeLine(1, 3)
makeLine(2, 5)

for(var i = 0; i <= 2*Math.PI; i += 2*Math.PI/number){
	ctx.strokeStyle = "#326b51"
	ctx.beginPath()
	ctx.arc(dis*Math.cos(i) + 400, dis*Math.sin(i) + 400, radius, 0, 2*Math.PI)
	ctx.fillStyle = "#9cd4ba"
	ctx.fill()
	ctx.stroke()
	ctx.fillStyle= "#326b51"
	ctx.font = "30px Verdana";
	ctx.fillText(names[i/(2*Math.PI/number)], dis*Math.cos(i) + 380, dis*Math.sin(i) + 410);
}