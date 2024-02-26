submitButton.addEventListener('click', (event) => {   
  $('#field_of_study').change(function() {
    var fieldId = $(this).val();
    $('#skills option').hide();
    $('#skills option[data-field="' + fieldId + '"]').show();
  });
});

  