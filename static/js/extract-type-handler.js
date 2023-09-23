function checkType() {
    var type = document.getElementById('extract_type').value;
    if (type === 'parameters' || type === 'indicators') {
        document.getElementById('namesDiv').style.display = 'block';
    } else {
        document.getElementById('namesDiv').style.display = 'none';
    }
}
