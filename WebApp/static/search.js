function myFunction() {
  // Declare variables
  var input, filter, tr, name, a, i, txtValue;
  input = document.getElementById("input");
  filter = input.value.toUpperCase();
  tr = document.getElementsByTagName("tr");
  name = document.getElementsByClassName("name");

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < name.length; i++) {
    a = name[i];
    console.log(a);
    txtValue = a.textContent || a.innerText;
    console.log(txtValue.toUpperCase().indexOf(filter));
    console.log(tr[i]);
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      tr[i+1].style.display = "";
    } else {
      tr[i+1].style.display = "none";
    }
  }
}
