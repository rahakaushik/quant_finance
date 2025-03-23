<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>STOCKER: Stalking the Stock Market</title>
    </head>
    <body>
       
        <html><title>Options Strategies</title>
        
        <!--script src="sorttable.js"></script>
        <style>
            /* Sortable tables */
            table.sortable thead {
            background-color:#eee;
            color:#666666;
            font-weight: bold;
            cursor: default;
           }
            
        </style-->            
         <?php
        require_once('simple_html_dom.php');
         error_reporting(E_ERROR | E_PARSE);
            
        // put your code here
        parse_str(implode('&', array_slice($argv, 1)), $_GET);
        $mode = $_GET ['mode'];
        if ($mode==1) {
            $single_symb = $_GET['symbol'];
        }
        $date_op = $_GET['dateop'];
        if($date_op==1) {
            $expdate = $_GET['expdate'];
            $exp_day = substr($expdate,2,2);
            $exp_mon = substr($expdate,0,2);
            $exp_year = substr($expdate,4,4);
        }
        //echo "$exp_day, $exp_mon, $exp_year";
        $getindus = $_GET['iname'];
        if ($getindus == "basic") {
          $basicSymbolsFile = "basic-symbols.csv";   
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");
        } elseif ($getindus == "finance") {
          $basicSymbolsFile = "finance-symbols.csv";
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");             
        } elseif ($getindus == "healthcare") {
          $basicSymbolsFile = "healthcare-symbols.csv";
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");          
        } elseif ($getindus == "energy") {
          $basicSymbolsFile = "energy-symbols.csv";
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");          
        } elseif ($getindus == "technology") {
          $basicSymbolsFile = "technology-symbols.csv"; 
          $snpf = $getindus."-opions.csv";
          
          if (!file_exists($snpf)) fopen($snpf,"w");          
        } elseif ($getindus == "goods") {
          $basicSymbolsFile = "goods-symbols.csv";
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");          
        } elseif ($getindus == "services") {
          $basicSymbolsFile = "services-symbols.csv";
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");          
        } elseif ($getindus == "misc") {
          $basicSymbolsFile = "misc-symbols.csv";  
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");   
        } elseif ($getindus == "nyse") {
          $basicSymbolsFile = "nyse-line.csv";  
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");           
        } elseif ($getindus == "snp500") {
          $basicSymbolsFile = "snp500-line.csv";  
          $snpf = $getindus."-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");           
        } else {
          $basicSymbolsFile = "snp500-line.csv";  
          $snpf = "snp500-options.csv";
          if (!file_exists($snpf)) fopen($snpf,"w");          
        }
            
        if(!file_exists($snpf)) fclose($snpf);
        //$basicSymbolsOutf = "basic-symbols-output.csv";
        $fh = fopen($basicSymbolsFile, 'r');
        //$fo = fopen($basicSymbolsOutf,'w');
        $symbData = fread($fh, filesize($basicSymbolsFile));;
        fclose($fh);
        if($mode == 1) {
            $symbData = ",".$single_symb;
        }
        //echo $symbData;
        ?>
            
        <body><table class="sortable" border="1">
        
        
        <?php
        $symbols = explode(",",$symbData);
        $i = 1;
        $symbstrng = $symbols[0]."+";
        $tags = "sl1dyqks7c6p2vm4t7";
        
        $class = new compareImages();
        $imageApath[0] = "5-day/BLANK-crop.jpeg";
        $imageApath[1] = "5-day/CBLI-crop.jpeg";
        $imageApath[2] = "5-day/CERS-crop.jpeg";
        $imageApath[3] = "5-day/BLR-crop.jpeg";
        $imageApath[4] = "5-day/CGE-crop.jpeg";
        $imageApath[5] = "5-day/AXP-crop.jpeg";
        $imageApath[6] = "5-day/FAF-crop.jpeg";
        $imageApath[7] = "5-day/LEAF-crop.jpeg";
        $imageApath[8] = "5-day/MQT-crop.jpeg";
        $imageApath[9] = "5-day/NMT-crop.jpeg";
        $imageApath[10] = "5-day/MUS-crop.jpeg";
        
        for(;;){
            
          $symbols[$i];
          

            
            #5-day 
            $url = "http://charting.nasdaq.com/ext/charts.dll?2-1-14-0-0-75-03NA000000".$symbols[$i]."-&SF:1|00-BG=FFFFFF-BT=0-WD=250-HT=200-";
            print $url;
            #intraday
            #$url = "http://charting.nasdaq.com/ext/charts.dll?2-1-17-0-0-008001830-03NA000000".$symbols[$i]."-&SF:1|00-BG=FFFFFF-BT=0-WD=250-HT=200-";
            #30 day
            #$url = "https://charting.nasdaq.com/ext/charts.dll?2-1-14-0-0-51-03NA000000".$symbols[$i]."-&SF:1|5-BG=FFFFFF-BT=0-WD=250-HT=200-";
            $randn = substr(str_shuffle("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0, 10);
            $imgl = "tmp/$randn-$symbols[$i].gif";
            file_put_contents($imgl, file_get_contents($url));;
            $img = imagecreatefromgif($imgl);
            #$imgarea = imagesx($img) * imagesy($img);
          
            $imcrop = imagecreatetruecolor(220, 110);   //to create 5 day cropped maps; uncomment this and block below to generate
            imagecopy($imcrop, $img,0,0,0,15,220,100);
            imagejpeg($imcrop,"tmp/$randn-crop.jpeg");
            
            $best_sim = 8;
            $blank_similarity = 5;
            for($k=0;$k<10; $k++){  
                $similarity = $class->compare($imageApath[$k], "tmp/$randn-crop.jpeg");
                #echo "$symbols[$i] $randn $similarity\n";
                if($k==0) $blank_smiliarity = $similarity;
                if($similarity < $best_sim) $best_sim = $similarity;
            }
            #echo "$blank_similarity $best_sim\n";
            if($blank_smiliarity != 0 && $best_sim < 2) {  
                $symblist = $symblist.",".$symbols[$i];
            }
           
          #echo "$symblist";  
          $i++; 
          flush();
          if($i>=sizeof($symbols)) break;
          //break;
        }
        $symblist = substr($symblist,1);
        #echo "$symblist";  

        $tradier_quotes = get_tradier_quote($symblist);
        $trad_quotes = explode('<quote>',$tradier_quotes);
        foreach($trad_quotes as $trad_quote) {
           #echo $trad_quote;
           $tradier_html = str_get_html($trad_quote);
           foreach($tradier_html->find('symbol') as $element)  $sym = $element->innertext;
           foreach($tradier_html->find('volume') as $element)  $vol = $element->innertext;
           foreach($tradier_html->find('average_volume') as $element)  $av_vol = $element->innertext;
           foreach($tradier_html->find('week_52_high') as $element)  $hi_52 = $element->innertext;
           foreach($tradier_html->find('week_52_low') as $element)  $lo_52 = $element->innertext;
           foreach($tradier_html->find('last') as $element)  $lst = $element->innertext;
           $volr = $vol/$av_vol;
           $mar52 = $hi_52-$lst/$lst-$lo_52;
           if($av_vol > 100000){
             print "ALERT: $sym $av_vol $mar52\n";
           } 
        }

        echo "\n</table></body></html>";
        //fclose($fo);
        
        
        
class compareImages 
{ 
    private function mimeType($i) 
    { 
        /*returns array with mime type and if its jpg or png. Returns false if it isn't jpg or png*/ 
        $mime = getimagesize($i); 
        $return = array($mime[0],$mime[1]); 
      
        switch ($mime['mime']) 
        { 
            case 'image/jpeg': 
                $return[] = 'jpg'; 
                return $return; 
            case 'image/png': 
                $return[] = 'png'; 
                return $return; 
            default: 
                return false; 
        } 
    } 
    
    private function createImage($i) 
    { 
        /*retuns image resource or false if its not jpg or png*/ 
        $mime = $this->mimeType($i); 
      
        if($mime[2] == 'jpg') 
        { 
            return imagecreatefromjpeg ($i); 
        } 
        else if ($mime[2] == 'png') 
        { 
            return imagecreatefrompng ($i); 
        } 
        else 
        { 
            return false; 
        } 
    } 
    
    private function resizeImage($i,$source) 
    { 
        /*resizes the image to a 8x8 squere and returns as image resource*/ 
        $mime = $this->mimeType($source); 
      
        $t = imagecreatetruecolor(8, 8); 
        
        $source = $this->createImage($source); 
        
        imagecopyresized($t, $source, 0, 0, 0, 0, 8, 8, $mime[0], $mime[1]); 
        
        return $t; 
    } 
    
    private function colorMeanValue($i) 
    { 
        /*returns the mean value of the colors and the list of all pixel's colors*/ 
        $colorList = array(); 
        $colorSum = 0; 
        for($a = 0;$a<8;$a++) 
        { 
        
            for($b = 0;$b<8;$b++) 
            { 
            
                $rgb = imagecolorat($i, $a, $b); 
                $colorList[] = $rgb & 0xFF; 
                $colorSum += $rgb & 0xFF; 
                
            } 
            
        } 
        
        return array($colorSum/64,$colorList); 
    } 
    
    private function bits($colorMean) 
    { 
        /*returns an array with 1 and zeros. If a color is bigger than the mean value of colors it is 1*/ 
        $bits = array(); 
         
        foreach($colorMean[1] as $color){$bits[]= ($color>=$colorMean[0])?1:0;} 

        return $bits; 

    } 
    
    public function compare($a,$b) 
    { 
        /*main function. returns the hammering distance of two images' bit value*/ 
        $i1 = $this->createImage($a); 
        $i2 = $this->createImage($b); 
        
        if(!$i1 || !$i2){return false;} 
        
        $i1 = $this->resizeImage($i1,$a); 
        $i2 = $this->resizeImage($i2,$b); 
        
        imagefilter($i1, IMG_FILTER_GRAYSCALE); 
        imagefilter($i2, IMG_FILTER_GRAYSCALE); 
        
        $colorMean1 = $this->colorMeanValue($i1); 
        $colorMean2 = $this->colorMeanValue($i2); 
        
        $bits1 = $this->bits($colorMean1); 
        $bits2 = $this->bits($colorMean2); 
        
        $hammeringDistance = 0; 
        
        for($a = 0;$a<64;$a++) 
        { 
        
            if($bits1[$a] != $bits2[$a]) 
            { 
                $hammeringDistance++; 
            } 
            
        } 
          
        return $hammeringDistance; 
    } 
} 

function get_tradier_quote($symblist) {
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://sandbox.tradier.com/v1/markets/quotes?symbols='.$symblist.'&greeks=false');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');

$headers = array();
$headers[] = 'Authorization: Bearer PP1XerfFMh97HbpxjkGpEf5FZvTL';
$headers[] = 'Accept: application/csv';

curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$result = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
if (curl_errno($ch)) {
    echo 'Error:' . curl_error($ch);
}
curl_close ($ch);
#echo $http_code;
return $result;

}
       
        ?>
        
        
    </body>
</html>
  
