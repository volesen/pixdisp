var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on("connect", function() {
	socket.emit("user", {data: 'I\'m connected!'});
});
socket.on('setPixel', function(pixel) {
	setPixel(pixel);
});
socket.on('hej', function(pixel) {
	pixel = JSON.parse(pixel);
	setPixel(pixel);
});
var currentColor = 'rgb(0, 0, 0)';
function setColor(selectedColor) {
	currentColor = selectedColor.style.backgroundColor;
};
function setPixel(pixel) {
	document.getElementById("canvas").rows[pixel.y].cells[pixel.x].style.backgroundColor = pixel.color;
};
function drawPixel(pixel) {
	socket.emit('drawPixel', {"x": pixel.cellIndex, "y": pixel.parentNode.rowIndex, "color": currentColor});
};