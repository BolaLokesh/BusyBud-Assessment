// Initialize cURL session with the given API endpoint URL
$ch = curl_init('https://coderbyte.com/api/challenges/json/age-counting');

// Set cURL options:
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);  // Return the response as a string instead of outputting it
curl_setopt($ch, CURLOPT_HEADER, 0);  // Don't include the header in the response

// Execute the cURL request and get the response
$data = curl_exec($ch);

// Close the cURL session
curl_close($ch);

// Decode the JSON response into a PHP associative array
$response = json_decode($data, true);

// Extract the 'data' key from the decoded response, which contains the raw string with age data
$dataString = $response['data'];

// Split the string into an array of items using ', ' as the delimiter
$items = explode(", ", $dataString);

// Initialize a counter for people aged 50 or older
$count = 0;

// Iterate through each item in the array
foreach ($items as $item) {
    // Check if the item contains the substring 'age='
    if (strpos($item, 'age=') !== false) {
        // Extract the age value by splitting the string around 'age=' and converting it to an integer
        $age = (int)str_replace('age=', '', explode("age=", $item)[1]);

        // If the extracted age is 50 or older, increment the count
        if ($age >= 50) {
            $count++;
        }
    }
}

// Output the final count of people aged 50 or older
echo $count;
