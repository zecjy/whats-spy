<?php
exec("pgrep -f start.py", $pids);
if(count($pids)>1) {
    echo "Process running.";
} else {
    echo "Process not running.";
}
?>