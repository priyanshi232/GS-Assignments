<!-- 1. Write a PHP script to set a cookie named "username" with the value "Gulnara Serik" and an expiration time of one hour.
-->
<?php
$cookieName = "username";
$cookieValue = "priyanshi";
$expirationTime = time() + 3600; // current time + 1 hour

setcookie($cookieName, $cookieValue, $expirationTime);

echo "Cookie named 'username' has been set with the value 'Gulnara Serik'.";
?>


<!-- 2. Write a PHP script to retrieve and display the value of the cookie named "username". -->
<?php
$cookieName = "username";

if (isset($_COOKIE[$cookieName])) {
    $cookieValue = $_COOKIE[$cookieName];
    echo "Value of cookie 'username': " . $cookieValue;
} else {
    echo "Cookie 'username' not found.";
}
?>

<!-- 3. Write a PHP script to delete a cookie named "username". -->
<?php
$cookieName = "username";

// Set the cookie expiration time to the past to delete the cookie
setcookie($cookieName, "", time() - 3600);

echo "Cookie named 'username' has been deleted.";
?>

<!-- 4. Write a PHP script to set a session variable named "userid" with the value 10020. -->
<?php
session_save_path('i:/custom/');
session_start();

$_SESSION["userid"] = 10020;

echo "Session variable 'userid' has been set with the value 10020.";
?>


<!-- 5. Write a PHP script to retrieve and display the value of the session variable "userid". -->
<?php
session_save_path('i:/custom/');
session_start();
if (isset($_SESSION["userid"])) {
    $userid = $_SESSION["userid"];
    echo "Value of session variable 'userid': " . $userid;
} else {
    echo "Session variable 'userid' not found.";
}
?>


<!-- 6. Write a PHP script to destroy a session and unset all session variables. -->
<?php
session_save_path('i:/custom/');
session_start();
$_SESSION = [];
session_destroy();

echo "Session destroyed. All session variables have been unset.";
?>


<!-- 7. Write a PHP script to set a secure cookie that can only be transmitted over an encrypted connection. -->
<?php
$cookieName = "my_Cookie";
$cookieValue = "Example_cookie_value";
$expirationTime = time() + 3600; // current time + 1 hour
$secureOnly = true; 
setcookie($cookieName, $cookieValue, $expirationTime, "/", "", $secureOnly, true);

echo "Secure cookie named 'my_Cookie' has been set.";
?>

<!-- 8. Write a PHP script to check if a cookie named "visited" exists. If it does, display a welcome message; otherwise, display a default message. -->
<?php
$cookieName = "visited";

if (isset($_COOKIE[$cookieName])) {
    echo "Welcome back! You have visited before.";
} else {
    echo "Welcome! This is your first visit.";
}

?>

<!-- 9. Write a PHP script to store an array of user preferences in a session variable. -->
<?php
session_save_path('i:/custom/');
session_start();
$userPreferences = array(
    "theme" => "dark",
    "language" => "hindi",
    "notifications" => true
);

$_SESSION["preferences"] = $userPreferences;

echo "User preferences have been stored in the session variable 'preferences'.";

?>


<!-- 10. Write a PHP script to retrieve and display user preferences stored in the session variable. -->
<?php
session_save_path('i:/custom/');
session_start();

if (isset($_SESSION["preferences"]))
{
    $userPreferences = $_SESSION["preferences"];

    echo "User Preferences:</br>";
    foreach ($userPreferences as $key => $value) {
        echo $key . ": " . $value . "</br>";
    }
 }
else
{
    echo "No user preferences found.";
}

?>

<!-- 11. Write a PHP script to set a session timeout after 30 minutes of inactivity. -->
<?php
session_save_path('i:/custom/');
session_start();

$sessionTimeout = 1800; // 30 minutes
if (isset($_SESSION['LAST_ACTIVITY'])) {
    $lastActivity = $_SESSION['LAST_ACTIVITY'];
    $currentTime = time();
    $timeSinceLastActivity = $currentTime - $lastActivity;
    if ($timeSinceLastActivity > $sessionTimeout) {
        session_unset();
        session_destroy();
        echo "Session expired. Please log in again.";
    } else {
        $_SESSION['LAST_ACTIVITY'] = $currentTime;
        echo "Session active.";
    }
} else {
    $_SESSION['LAST_ACTIVITY'] = time();
    echo "Session started.";
}
?>

<!-- 12. Write a PHP script to display the number of active sessions on the server. -->
<?php
session_save_path('i:/custom/');

$sessionSavePath = session_save_path();
$sessionFiles = glob($sessionSavePath . '/*');
$activeSessions = 0;
foreach ($sessionFiles as $sessionFile) {
    if (is_file($sessionFile) && filectime($sessionFile) + ini_get('session.gc_maxlifetime') > time()) {
        $activeSessions++;
    }
}                        
echo "Number of active sessions: " . $activeSessions;
?>


<!-- 13. Write a PHP script to limit the maximum number of concurrent sessions for a user to 3. -->
<?php
session_save_path('i:/custom/');
session_start();

$maxSessions = 3; 
if (!isset($_SESSION['session_count'])) {
    $_SESSION['session_count'] = 1;
} else {
    $_SESSION['session_count']++;

    if ($_SESSION['session_count'] > $maxSessions) {
        session_unset();
        session_destroy();
        echo "Maximum session limit exceeded. Please log in again.";
        exit;
    }
}
echo "Session active. Session count: " . $_SESSION['session_count'];

?>

<!-- 14. Write a PHP script to regenerate the session ID to prevent session fixation attacks. -->
<?php
session_save_path('i:/custom/');
session_start();
session_regenerate_id(true);
echo "Session ID has been regenerated.";
?>

<!-- 15. Write a PHP script to display the last time the session was accessed by the user. -->
<?php
session_save_path('i:/custom/');
session_start();
session_regenerate_id(true);

echo "Session ID has been regenerated.";

?>

<!-- 16. Write a PHP script to set a cookie and a session variable with the same name. Display their values to compare. --> -->
<?php
session_save_path('i:/custom/');
$cookieName = "myCookie";
$value = "Cookie Value";
setcookie($cookieName, $value, time() + 3600, "/");
session_start();
$_SESSION[$cookieName] = $value;
echo "Cookie value: " . $_COOKIE[$cookieName] . "";
echo "Session variable value: " . $_SESSION[$cookieName];

?>
