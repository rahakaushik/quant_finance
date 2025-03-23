<?php
parse_str(implode('&', array_slice($argv, 1)), $_GET);
$sector = $_GET['sector'];
$optype = $_GET['optype'];
$mode = $_GET['mode'];
#$view = $_GET['view'];
if ($optype == "otm") {
    
    $f = file_get_contents($sector."-".$optype."_profit.csv");
    #echo $f;
    $file_line_array = explode("\n", $f);
    $num_lines = count($file_line_array);
    $lt5K_blurb = "";
    $num_lt5k = 0;
    $lt15K_blurb = "";
    $num_lt15k = 0;
    $num_lt50k = 0;
    $lt50K_blurb = "";
    
    if($mode == "freeview") $num_ideas = 20;
    if($mode == "premium")  $num_ideas = $num_lines;
    
    for ($i=0;$i<=$num_ideas;$i++) 
    
    {
        
        if(!isset($file_line_array[$i])) { $file_line_array[$i] = null; }
        $line = $file_line_array[$i];
        #echo $line;
        if($i > 0) {
        
        $linedata = explode(",", $line);
        #echo count($linedata);
//        for($j=0;$j<=count($linedata);$j++) 
//        {
//            if(!isset($linedata[$j])) {$linedata[$j] = null;}
//        }
        if(!isset($linedata[3])) {$linedata[3] = null;}
        if(!isset($linedata[2])) {$linedata[2] = null;}
        if(!isset($linedata[7])) {$linedata[7] = null;}
        if(!isset($linedata[8])) {$linedata[8] = null;}
        if(!isset($linedata[10])) {$linedata[10] = null;}
        //$income_gen = floatval($linedata[7]);
        //print "$linedata[3]\n";
        if($linedata[7] > 0.0) {
                //print($linedata[8]);
        if($linedata[3] <= 5000.0)  {
            //echo "this is $linedata[0]";
            //exit();
            $num_lt5k = $num_lt5k+1;
            $lt5K_blurb = $lt5K_blurb."<font color='black'>If you have $".number_format(floatval($linedata[3]),0)." to hold as collateral till the expiration date of ".
            $linedata[10].", <b>selling a put option</b> of <b>".$linedata[0]."</b> will generate an <b>income of $".number_format(floatval($linedata[7]),0).
            "</b> at a $".$linedata[2]." strike price</font>.<br><font size=2>If the stock trades above $".$linedata[2]." on expiration date, you will"
            . " keep the premium of $".number_format(floatval($linedata[7]),0)." as income. If ".$linedata[0]." trades at or below $".$linedata[2]." then 100 shares"
            . " will be assigned to you, at the market price on expiration date. The breakeven point is $".$linedata[8]." so if price at expiration is above breakeven "
            . " profits will be generated. The stock was last trading at ".$linedata[1]." </font></p><p>";
            
             
        }
        if (nBetween($linedata[3], 15000.0, 5000.0))  {
            //echo "this is $linedata[0]";
            //exit();
            $num_lt15k = $num_lt15k+1;
            $lt15K_blurb = $lt15K_blurb."<font color='black'>If you have $".number_format(floatval($linedata[3]),0)." to hold as collateral till the expiration date of ".
            $linedata[10].", <b>selling a put option</b> of <b>".$linedata[0]."</b> will generate an <b>income of $".number_format(floatval($linedata[7]),0).
            "</b> at a $".$linedata[2]." strike price.</font><br><font size=2> If the stock trades above $".$linedata[2]." on expiration date, you will"
            . " keep the premium of $".number_format(floatval($linedata[7]),0)." as income. If ".$linedata[0]." trades at or below $".$linedata[2]." then 100 shares"
            . " will be assigned to you, at the market price on expiration date. The breakeven point is $".$linedata[8]." so if price at expiration is above breakeven "
            . " profits will be generated. The stock was last trading at ".$linedata[1]." </font></p><p>";
            
             
        }
        if (nBetween($linedata[3], 50000.0, 15000.0))  {
            //echo "this is $linedata[0]";
            //exit();
            $num_lt50k = $num_lt50k+1;
            $lt50K_blurb = $lt50K_blurb."<font color='black'>If you have $".number_format(floatval($linedata[3]),0)." to hold as collateral till the expiration date of ".
            $linedata[10].", <b>selling a put option</b> of <b>".$linedata[0]."</b> will generate an <b>income of $".number_format(floatval($linedata[7]),0).
            "</b> at a $".$linedata[2]." strike price.</font><br><font size=2> If the stock trades above $".$linedata[2]." on expiration date, you will"
            . " keep the premium of $".number_format(floatval($linedata[7]),0)." as income. If ".$linedata[0]." trades at or below $".$linedata[2]." then 100 shares"
            . " will be assigned to you, at the market price on expiration date. The breakeven point is $".$linedata[8]." so if price at expiration is above breakeven "
            . " profits will be generated. The stock was last trading at ".$linedata[1]." </font></p><p>";
            
             
        }
        if (nBetween($linedata[3], 100000.0, 50000.0))  {
                //echo "this is $linedata[0]";
                //exit();
                $num_lt50k = $num_lt50k+1;
                $lt50K_blurb = $lt50K_blurb."<font color='black'>If you have $".number_format(floatval($linedata[3]),0)." to hold as collateral till the expiration date of ".
                $linedata[10].", <b>selling a put option</b> of <b>".$linedata[0]."</b> will generate an <b>income of $".number_format(floatval($linedata[7]),0).
                "</b> at a $".$linedata[2]." strike price.</font><br><font size=2> If the stock trades above $".$linedata[2]." on expiration date, you will"
                . " keep the premium of $".number_format(floatval($linedata[7]),0)." as income. If ".$linedata[0]." trades at or below $".$linedata[2]." then 100 shares"
                . " will be assigned to you, at the market price on expiration date. The breakeven point is $".$linedata[8]." so if price at expiration is above breakeven "
                . " profits will be generated. The stock was last trading at ".$linedata[1]." </font></p><p>";
                
                 
            }
        }
       }
    }
}
//echo $num_lt5k;
//if($num_lt5k-2 > 0) echo $lt5K_blurb;
//if($num_lt15k-2 > 0) echo $lt15K_blurb;

//print "$num_lt50k  $num_lt5k $num_lt15k";

function nBetween($varToCheck, $high, $low) {
if($varToCheck < $low) return false;
if($varToCheck > $high) return false;
return true;
}
?>

<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Options Blog</title>
		<meta name="description" content="Blueprint: Nested Accordion" />
		<meta name="keywords" content="nested, accordion, simple, vertical, web development, css3, javascript" />
		<meta name="author" content="Codrops" />
		<link rel="shortcut icon" href="../favicon.ico">
		<link rel="stylesheet" type="text/css" href="css/default.css" />
		<!--link rel="stylesheet" type="text/css" href="http://qntafi.com/wp-content/themes/quantifi/css/accordion/css/acc-component.css" /-->
		<link rel="stylesheet" type="text/css" href="css/component.css" />
                <script src="js/modernizr.custom.js"></script>
                
	</head>
	<body>
		<div class="container">
			<header class="clearfix">
				<span>QNTAFI</span>
				<h1>Premium</h1>
                
                                
				<!--nav>
					<a href="http://tympanus.net/Blueprints/VerticalIconMenu/" class="icon-arrow-left" data-info="previous Blueprint">Previous Blueprint</a>
					<a href="http://tympanus.net/codrops/?p=14588" class="icon-drop" data-info="back to the Codrops article">back to the Codrops article</a>
				</nav-->
			</header>	
                    
			<div class="main">
                            <p><font color="black">
                            Options income trade ideas by selling Put options. Selling a put option is equivalent to buying rights to purchase a stock at a pre-determined price or strike price. A premium is paid as credit to the seller of the put option. If the stock trades above the strike price then the option expires out of money and the seller gets to keep the premium. 
                            <?php echo "This report was generated on ". date("Y-m-d")." ";?>
                            </font>
                            </p>	
                            
                                <ul id="cbp-ntaccordion" class="cbp-ntaccordion">
					<li>
						<h3 class="cbp-nttrigger">S&P500 Options</h3>
						<div class="cbp-ntcontent">
							<p>S&P500 put selling strategies for generating income for options which have expiration dates this week. The premium offerings shows all income generation ideas. The trades are classified by amount of collateral needed. Disclaimer: options have risk associated and selling puts can have unlimited loss if the price of the security crashes.
                                                            
                                                        <ul class="cbp-ntsubaccordion">
								<li>
									<h4 class="cbp-nttrigger">Collateral of $5K</h4>
									<div class="cbp-ntcontent">
										<p> <?php 
                                                                                if($num_lt5k -2 > 0) echo $lt5K_blurb;
                                                                                        ?>
                                                                                </p>
									</div>
								</li>
								<li>
									<h4 class="cbp-nttrigger">Collateral of $15K</h4>
									<div class="cbp-ntcontent">
										<p> <?php 
                                                                                if($num_lt15k -2 > 0) echo $lt15K_blurb;
                                                                                        ?>
                                                                                </p>
                                                                        </div>
								</li>
								<li>
									<h4 class="cbp-nttrigger">Collateral of $50K+</h4>
									<div class="cbp-ntcontent">
										<p> <?php 
                                                                                if($num_lt50k -2 > 0) echo $lt50K_blurb;
                                                                                        ?>
                                                                                </p>
                                                                        </div>
								</li>
							</ul>
						</div>
					</li>
					<li>
						<h3 class="cbp-nttrigger">Find more ideas</h3>
						<div class="cbp-ntcontent">
							<p>Our members have access to many other actionable ideas generated using variety of different options strategies that are executed algorithmically on delayed and real time data.
                                                        If you already have membership please go ahead and access our Options offering. If not register with a membership plan</p>
							<ul class="cbp-ntsubaccordion">
								<li>
									<h4 class="cbp-nttrigger">Sign up for Qntafi GOLD</h4>
									<div class="cbp-ntcontent">
                                                                            <p></p>
                                                                        </div>
								</li>
								
							</ul>
						</div>
					</li>
					
					
				</ul>
			</div>
		</div>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
		<script src="js/jquery.cbpNTAccordion.min.js"></script>
                
		<script>
			$( function() {
				/*
				- how to call the plugin:
				$( selector ).cbpNTAccordion( [options] );
				- destroy:
				$( selector ).cbpNTAccordion( 'destroy' );
				*/

				$( '#cbp-ntaccordion' ).cbpNTAccordion();

			} );
		</script>
	</body>
</html>
