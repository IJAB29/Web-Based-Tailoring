function toggleRequired(parentName) {
  var parent = document.getElementById(parentName);
  var inputElements =  parent.querySelectorAll('input');

  inputElements.forEach(function(inputElement) {
    if (inputElement.offsetParent === null) {
      inputElement.required = false;
      inputElement.value = "";
    } else {
      inputElement.required = true;
    }
  });
}

function showForm(checkbox, containerName) {

  if (checkbox.checked) {
    containerName.style.display = "block";
  } else {
    containerName.style.display = "none";
  }
  toggleRequired(containerName.id);
}

function validateForm() {
  var checkbox1 = document.getElementById('dressShirtsCheckbox');
  var checkbox2 = document.getElementById('slacksCheckbox');
  var checkbox3 = document.getElementById('skirtsCheckbox');

  if (!checkbox1.checked && !checkbox2.checked && !checkbox3.checked) {
    alert('Please select at least one checkbox');
    return false;
  }

  return true;
}
