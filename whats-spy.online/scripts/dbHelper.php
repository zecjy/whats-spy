<?php
$ids = explode(",",$_GET['id']);
$type = $_GET['type'];
$db = new mysqli('localhost', 'wa_logger', '', 'whats-spy');
$hash_key = "kinda_safe_string:D";
$hash = md5($_GET['id'] . $hash_key);

if($_GET['key'] !== $hash) {
    die('wrong key');
}

if($db->connect_error) {
    die("MySQL connection failed.");
}

if($_GET['id'] === "all") {
    $ids = $db->query("SELECT id FROM numbers")->fetch_all(MYSQLI_NUM);
    foreach($ids as $key=>$id) {
        $ids[$key] = $id[0];
    }
}

foreach($ids as $key=>$id) {
    $data_all[$key]['logs'] = $db->query("SELECT time, online FROM logs WHERE number_id =".$id." AND time > (SELECT time from script_starts order by time desc limit 1)")->fetch_all(MYSQLI_ASSOC);
    //$data_all[$key]['logs'] = $db->query("SELECT time, online FROM logs WHERE number_id =".$id." AND time < 1511789299")->fetch_all(MYSQLI_ASSOC);
    $data_all[$key]['name'] = $db->query("SELECT name FROM numbers WHERE id=".$id)->fetch_all(MYSQLI_ASSOC)[0]['name'];
}

$data_out = [];

if($type == "1") {
    foreach($data_all as $key=>$data) {
        for($i=0; $i<count($data['logs']); $i++) {
            if($data['logs'][$i]['online'] == '1' && ($data['logs'][$i+1]['online'] == '0') && ($data['logs'][$i]['time'] < $data['logs'][$i+1]['time'])) {// || $data['logs'][$i+1]['online'] == '1')) {
                $point = [];
                $point[] = $data['name'];//"Person ".$key;//
                $point[] = $data['logs'][$i]['time']*1000;
                $point[] = $data['logs'][$i+1]['time']*1000;
                $data_out[] = $point;
            }
        }
    }
} else if($type == "2") {
    foreach($data_all as $key=>$data) {
        $points = [];
        for($i=0; $i<count($data['logs']); $i++) {
            if($data['logs'][$i]['online'] == '1' && ($data['logs'][$i+1]['online'] == '0') && ($data['logs'][$i]['time'] < $data['logs'][$i+1]['time'])) {// || $data['logs'][$i+1]['online'] == '1')) {
                $point = [];
                $point['start'] = $data['logs'][$i]['time']*1000;
                $point['end'] = $data['logs'][$i+1]['time']*1000;
                $point['name'] = $data['name'];
                $points[] = $point;
            }
        }
        $data_out[$key]['category'] = $data['name'];
        $data_out[$key]['segments'] = $points;
    }
}

echo json_encode($data_out);
?>