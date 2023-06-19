// Connect to the Socket.IO server
const socket = io();

// Listen for the 'data' event from the server
socket.on('data', function(data) {
  // Update elements on the page with the new data
  document.getElementById('cpu').textContent = 'CPU Usage: ' + data.cpu + '%';
  document.getElementById('cpu_temp').textContent = 'CPU Temp: ' + data.cpu_temp + '(Celsius)';
  document.getElementById('ram').textContent = 'RAM Usage: ' + data.ram + '%';
  document.getElementById('ram_temp').textContent = 'RAM Temp: ' + data.ram_temp + '(Celsius)';
  document.getElementById('gpu').textContent = 'GPU Usage: ' + data.gpu + '%';
  document.getElementById('gpu_temp').textContent = 'GPU Temp: ' + data.gpu_temp + '(Celsius)';
  document.getElementById('nvme_temp').textContent = 'NVME Temp: ' + data.nvme_temp + '(Celsius)';
});
