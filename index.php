<html>
<head></head>
<body>
<form action="index.php" method="post">
  <input type="text" name="recherche" placeholder="exemple:Chat" /></p>
  <p><input type="submit" value="OK"></p>
</form>

<?php
//1 - Settings (please update to math your own)
$consumer_key='HzZpvfMusPz9rOujU6XAjruBW'; //Provide your application consumer key
$consumer_secret='oJ9IdjidamiZC1HZTO7gyRvrVcyHXKyaDkM7TdCOhAy3bgE7JS'; //Provide your application consumer secret
$oauth_token = '960464454252187653-hq9PoZZ81wisLPjt2xA6ogEgq5Ic6cG'; //Provide your oAuth Token
$oauth_token_secret = 'NcvGN0Lln0F4MD730krA94TFl2jlCfxbQ1v1ZcK6XAyOk'; //Provide your oAuth Token Secret
//2 - Include @abraham's PHP twitteroauth Library
require "twitteroauth/autoload.php";

use Abraham\TwitterOAuth\TwitterOAuth;
//3 - Authentication
/* Create a TwitterOauth object with consumer/user tokens. */
$connection = new TwitterOAuth($consumer_key, $consumer_secret, $oauth_token, $oauth_token_secret);
$content = $connection->get("account/verify_credentials");
//4 - Start Querying
if( isset($_POST['recherche']) )
{
     $recherche = $_POST['recherche'];
     $statuses = $connection->get("search/tweets", ["q" => $recherche, "lang" => "fr","count" => 90, "exclude_replies" => true,"in_reply_to_status_id"=>null,"tweet_mode"=>"extended","display_text_range"=>140,280]);
     //foreach ($statuses-> as $result) {
     foreach ($statuses->statuses as $tweet) {
       $tweet_content = $tweet->full_text;
       if(!strstr($tweet_content,"RT")){
         printf($tweet_content.'</br>');
       }

     }

}



//}
?>
</body>
</html>
