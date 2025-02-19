<?php
use Bitrix\Main\Diag;


CModule::IncludeModule('iblock');
$path = $_SERVER['DOCUMENT_ROOT'] . '/req-log.txt';
if($_REQUEST['auth']['application_token'] == 'er0l1heeqiqo443e81zmaoigsf6d26cf') {
	$message = (new Diag\LogFormatter())->format("{req}\n{trace}\n{delimiter}\n", [
		'req' => $_REQUEST['data']['FIELDS']['ID'],
		'trace' => Diag\Helper::getBackTrace(20, DEBUG_BACKTRACE_IGNORE_ARGS, 2),
	]);
	(new Diag\FileLogger($path))->error($message);

}