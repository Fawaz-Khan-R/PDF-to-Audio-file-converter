document.addEventListener('DOMContentLoaded', function() {
    var scanningOption = document.getElementById('scanning_option');
    var pageRangeFields = document.getElementById('page_range_fields');
    var keywordFields = document.getElementById('keyword_specific_fields');

    // Function to toggle visibility of additional fields based on selected option
    function toggleAdditionalFields() {
        var option = scanningOption.value;

        if (option === 'page_range') {
            pageRangeFields.style.display = 'block';
            keywordFields.style.display = 'none';
        } else if (option === 'keyword_specific') {
            pageRangeFields.style.display = 'none';
            keywordFields.style.display = 'block';
        } else {
            pageRangeFields.style.display = 'none';
            keywordFields.style.display = 'none';
        }
    }

    // Event listener to trigger toggling when option changes
    scanningOption.addEventListener('change', toggleAdditionalFields);

    // Initial call to toggle additional fields based on default selected option
    toggleAdditionalFields();
});
