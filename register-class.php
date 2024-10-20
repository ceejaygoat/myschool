<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $grade = $_POST['grade'];
    $absent_students = $_POST['absent_students']; // Array of absent student IDs

    // Save absenteeism records to a file or database (simplified here)
    $data = "Grade: $grade | Absent Students: " . implode(", ", $absent_students) . "\n";
    file_put_contents('absenteeism_records.txt', $data, FILE_APPEND);

    echo "Absenteeism registered for Grade $grade.";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Class (Absenteeism)</title>
</head>
<body>
    <h2>Register Class Absenteeism</h2>
    <form method="POST" action="register-class.php">
        <label for="grade">Grade:</label>
        <select name="grade" required>
            <option value="Grade 10">Grade 10</option>
            <option value="Grade 11">Grade 11</option>
            <option value="Grade 12">Grade 12</option>
        </select><br>

        <label for="absent_students">Absent Students (IDs separated by commas):</label><br>
        <textarea name="absent_students" required></textarea><br>

        <button type="submit">Register Absenteeism</button>
    </form>
</body>
</html>
