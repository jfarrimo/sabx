###############################################################################
#
# sabx10.oxm - an SABX file manipulation library
# Copyright (C) 2009, 2010 Jay Farrimond (jay@sabikerides.com)
#
# This file is part of sabx10.oxm.
#
# sabx10.oxm is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# sabx10.oxm is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with sabx10.oxm.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

test_data = """<?xml version='1.0' encoding='utf-8'?>
<rideset xmlns="http://www.sabikerides.com/SABX/1/0/"
	 version="1.0">

  <uuid>147dbb84-d109-44f7-9ac2-09b2a736993f</uuid>
  <version>1</version>
  <zip_prefix>781</zip_prefix>

  <ride_type>road</ride_type>
  <title>Tour de Gruene 2009 Tour</title>
  <description><p>This is the tour route for the 2009 Tour de Gruene.  The time
      trial courses will have their own map.  Please note that the stops listed
      on this map are not the official rest areas for the ride.  Those will
      come later.  For now I have included the stops you would use if you did
      the ride on your own.</p>
    <p>Check out the <a href="http://www.tourdegruene.com/">Tour de Gruene web
	site</a> for more information.</p>
  </description>
  <terrain>Flat</terrain>

  <photos>
    <title>Returning via River Rd.</title>
    <src>http://farm4.static.flickr.com/3352/3639773356_2435f78398_m.jpg</src>
    <photo>
      <desc>2009-06-07 Gruene</desc>
      <href>http://www.flickr.com/photos/sabikerides/sets/72157619945875214/</href>
    </photo>
  </photos>

  <!-- ******************************************* -->
  <!-- parking                                     -->
  <!-- ******************************************* -->

  <parking id='1'>
    <description>Gruene has plenty of parking. Most of it is behind the shops
      on the corner of Gruene Rd. and Hunter Rd. on the south side of Hunter
      Rd. The earlier in the day you get there, the better chances of finding a
      good spot.</description>
    <lat>29.737931</lat>
    <lon>-98.103585</lon>
  </parking>

  <!-- ******************************************* -->
  <!-- turns & segements                           -->
  <!-- ******************************************* -->

  <turn id='1'>
    <fromto>parking to Hunter Rd.</fromto>
    <cue>RIGHT onto Gruene Rd.</cue>
    <comments>From the parking lot, turn right onto Gruene Rd.</comments>
  </turn>

  <segment id='2'>
    <road>Gruene Rd.</road>
    <fromto>parking to Hunter Rd.</fromto>
    <comments>Gruene Hall is on your left.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>20</speed>
    <waypoint id='6'>
      <lat>29.738246</lat>
      <lon>-98.103823</lon>
      <ele>213.6</ele>
      <usgs>206.44480896</usgs>
    </waypoint>
    <waypoint id='7'>
      <lat>29.738285</lat>
      <lon>-98.103958</lon>
      <ele>213.1</ele>
      <usgs>206.279098511</usgs>
    </waypoint>
    <waypoint id='8'>
      <lat>29.738286</lat>
      <lon>-98.103996</lon>
      <ele>212.6</ele>
      <usgs>206.126815796</usgs>
    </waypoint>
    <waypoint id='9' stop='0a'>
      <lat>29.738416</lat>
      <lon>-98.10415</lon>
      <ele>212.6</ele>
      <usgs>205.945068359</usgs>
    </waypoint>
  </segment>

  <turn id='2'>
    <fromto>Gruene Rd. to Hunter Rd.</fromto>
    <cue>RIGHT onto Hunter Rd.</cue>
    <comments>Hunter Rd. T's in on the right.</comments>
  </turn>

  <segment id='3'>
    <road>Hunter Rd.</road>
    <fromto>Gruene Rd. to FM 1102</fromto>
    <comments>You'll leave Gruene, cross over FM 306, then go through fields
      and houses.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='10'>
      <lat>29.738529</lat>
      <lon>-98.104135</lon>
      <ele>212.6</ele>
      <usgs>205.798934937</usgs>
    </waypoint>
    <waypoint id='11'>
      <lat>29.738557</lat>
      <lon>-98.104105</lon>
      <ele>212.1</ele>
      <usgs>205.798934937</usgs>
    </waypoint>
    <waypoint id='12'>
      <lat>29.738789</lat>
      <lon>-98.103762</lon>
      <ele>213.1</ele>
      <usgs>206.553848267</usgs>
    </waypoint>
    <waypoint id='13'>
      <lat>29.739032</lat>
      <lon>-98.103442</lon>
      <ele>214.0</ele>
      <usgs>206.764709473</usgs>
    </waypoint>
    <waypoint id='14'>
      <lat>29.739338</lat>
      <lon>-98.103105</lon>
      <ele>214.5</ele>
      <usgs>207.061416626</usgs>
    </waypoint>
    <waypoint id='15'>
      <lat>29.739712</lat>
      <lon>-98.102757</lon>
      <ele>215.5</ele>
      <usgs>207.666137695</usgs>
    </waypoint>
    <waypoint id='16'>
      <lat>29.740031</lat>
      <lon>-98.102515</lon>
      <ele>214.5</ele>
      <usgs>205.493041992</usgs>
    </waypoint>
    <waypoint id='17'>
      <lat>29.740543</lat>
      <lon>-98.102197</lon>
      <ele>212.6</ele>
      <usgs>204.518493652</usgs>
    </waypoint>
    <waypoint id='18'>
      <lat>29.741035</lat>
      <lon>-98.101898</lon>
      <ele>211.1</ele>
      <usgs>202.638534546</usgs>
    </waypoint>
    <waypoint id='19'>
      <lat>29.741559</lat>
      <lon>-98.101569</lon>
      <ele>210.2</ele>
      <usgs>203.046005249</usgs>
    </waypoint>
    <waypoint id='20'>
      <lat>29.741904</lat>
      <lon>-98.101284</lon>
      <ele>211.1</ele>
      <usgs>203.618713379</usgs>
    </waypoint>
    <waypoint id='21'>
      <lat>29.742246</lat>
      <lon>-98.100851</lon>
      <ele>210.7</ele>
      <usgs>204.030532837</usgs>
    </waypoint>
    <waypoint id='22'>
      <lat>29.742581</lat>
      <lon>-98.100334</lon>
      <ele>212.1</ele>
      <usgs>205.383483887</usgs>
    </waypoint>
    <waypoint id='23'>
      <lat>29.742944</lat>
      <lon>-98.099749</lon>
      <ele>212.1</ele>
      <usgs>205.549865723</usgs>
    </waypoint>
    <waypoint id='24'>
      <lat>29.743337</lat>
      <lon>-98.099126</lon>
      <ele>213.1</ele>
      <usgs>205.202529907</usgs>
    </waypoint>
    <waypoint id='25'>
      <lat>29.743682</lat>
      <lon>-98.098554</lon>
      <ele>212.6</ele>
      <usgs>205.649139404</usgs>
    </waypoint>
    <waypoint id='26'>
      <lat>29.743992</lat>
      <lon>-98.098044</lon>
      <ele>212.6</ele>
      <usgs>206.38949585</usgs>
    </waypoint>
    <waypoint id='27'>
      <lat>29.744072</lat>
      <lon>-98.097907</lon>
      <ele>212.1</ele>
      <usgs>206.587219238</usgs>
    </waypoint>
    <waypoint id='28'>
      <lat>29.74413</lat>
      <lon>-98.097812</lon>
      <ele>212.6</ele>
      <usgs>206.636810303</usgs>
    </waypoint>
    <waypoint id='29' stop='0'>
      <lat>29.744149</lat>
      <lon>-98.097777</lon>
      <ele>212.6</ele>
      <usgs>206.8412323</usgs>
    </waypoint>
    <waypoint id='30'>
      <lat>29.744447</lat>
      <lon>-98.097307</lon>
      <ele>213.1</ele>
      <usgs>206.865814209</usgs>
    </waypoint>
    <waypoint id='31'>
      <lat>29.744784</lat>
      <lon>-98.096784</lon>
      <ele>213.1</ele>
      <usgs>206.884994507</usgs>
    </waypoint>
    <waypoint id='32'>
      <lat>29.745151</lat>
      <lon>-98.096328</lon>
      <ele>213.6</ele>
      <usgs>206.799362183</usgs>
    </waypoint>
    <waypoint id='33'>
      <lat>29.745608</lat>
      <lon>-98.0958</lon>
      <ele>213.1</ele>
      <usgs>207.010314941</usgs>
    </waypoint>
    <waypoint id='34'>
      <lat>29.746094</lat>
      <lon>-98.095237</lon>
      <ele>214.0</ele>
      <usgs>207.470657349</usgs>
    </waypoint>
    <waypoint id='35'>
      <lat>29.746604</lat>
      <lon>-98.094648</lon>
      <ele>215.0</ele>
      <usgs>209.010192871</usgs>
    </waypoint>
    <waypoint id='36'>
      <lat>29.747081</lat>
      <lon>-98.094095</lon>
      <ele>216.9</ele>
      <usgs>210.167022705</usgs>
    </waypoint>
    <waypoint id='37'>
      <lat>29.747554</lat>
      <lon>-98.093551</lon>
      <ele>217.9</ele>
      <usgs>210.707672119</usgs>
    </waypoint>
    <waypoint id='38'>
      <lat>29.748015</lat>
      <lon>-98.09301</lon>
      <ele>218.4</ele>
      <usgs>211.078948975</usgs>
    </waypoint>
    <waypoint id='39'>
      <lat>29.748416</lat>
      <lon>-98.092548</lon>
      <ele>218.8</ele>
      <usgs>211.32270813</usgs>
    </waypoint>
    <waypoint id='40'>
      <lat>29.748876</lat>
      <lon>-98.092014</lon>
      <ele>218.8</ele>
      <usgs>211.535827637</usgs>
    </waypoint>
    <waypoint id='41'>
      <lat>29.749384</lat>
      <lon>-98.09142</lon>
      <ele>218.4</ele>
      <usgs>211.752624512</usgs>
    </waypoint>
    <waypoint id='42'>
      <lat>29.74974</lat>
      <lon>-98.091018</lon>
      <ele>218.8</ele>
      <usgs>211.892868042</usgs>
    </waypoint>
    <waypoint id='43'>
      <lat>29.749992</lat>
      <lon>-98.090929</lon>
      <ele>218.4</ele>
      <usgs>211.807403564</usgs>
    </waypoint>
    <waypoint id='44'>
      <lat>29.750182</lat>
      <lon>-98.091037</lon>
      <ele>218.4</ele>
      <usgs>211.66355896</usgs>
    </waypoint>
    <waypoint id='45'>
      <lat>29.750577</lat>
      <lon>-98.0915</lon>
      <ele>218.4</ele>
      <usgs>211.273971558</usgs>
    </waypoint>
    <waypoint id='46'>
      <lat>29.751058</lat>
      <lon>-98.092081</lon>
      <ele>218.4</ele>
      <usgs>210.73324585</usgs>
    </waypoint>
    <waypoint id='47'>
      <lat>29.751612</lat>
      <lon>-98.09275</lon>
      <ele>217.4</ele>
      <usgs>209.74420166</usgs>
    </waypoint>
    <waypoint id='48'>
      <lat>29.751841</lat>
      <lon>-98.093015</lon>
      <ele>216.9</ele>
      <usgs>209.146560669</usgs>
    </waypoint>
    <waypoint id='49'>
      <lat>29.752099</lat>
      <lon>-98.093129</lon>
      <ele>216.4</ele>
      <usgs>208.824356079</usgs>
    </waypoint>
    <waypoint id='50'>
      <lat>29.752284</lat>
      <lon>-98.093082</lon>
      <ele>216.9</ele>
      <usgs>208.771331787</usgs>
    </waypoint>
    <waypoint id='51'>
      <lat>29.752861</lat>
      <lon>-98.09276</lon>
      <ele>216.4</ele>
      <usgs>210.349914551</usgs>
    </waypoint>
    <waypoint id='52'>
      <lat>29.753324</lat>
      <lon>-98.092423</lon>
      <ele>216.0</ele>
      <usgs>212.076202393</usgs>
    </waypoint>
    <waypoint id='53'>
      <lat>29.753854</lat>
      <lon>-98.092015</lon>
      <ele>216.4</ele>
      <usgs>212.612854004</usgs>
    </waypoint>
    <waypoint id='54'>
      <lat>29.75443</lat>
      <lon>-98.091537</lon>
      <ele>217.4</ele>
      <usgs>213.154846191</usgs>
    </waypoint>
    <waypoint id='55'>
      <lat>29.754987</lat>
      <lon>-98.091035</lon>
      <ele>217.9</ele>
      <usgs>213.764205933</usgs>
    </waypoint>
    <waypoint id='56'>
      <lat>29.755454</lat>
      <lon>-98.090574</lon>
      <ele>218.8</ele>
      <usgs>214.205245972</usgs>
    </waypoint>
    <waypoint id='57'>
      <lat>29.756145</lat>
      <lon>-98.08992</lon>
      <ele>219.8</ele>
      <usgs>215.109176636</usgs>
    </waypoint>
    <waypoint id='58'>
      <lat>29.756724</lat>
      <lon>-98.089465</lon>
      <ele>221.7</ele>
      <usgs>217.370727539</usgs>
    </waypoint>
    <waypoint id='59'>
      <lat>29.757388</lat>
      <lon>-98.088962</lon>
      <ele>223.6</ele>
      <usgs>219.595565796</usgs>
    </waypoint>
    <waypoint id='60'>
      <lat>29.75789</lat>
      <lon>-98.088561</lon>
      <ele>225.6</ele>
      <usgs>220.334289551</usgs>
    </waypoint>
    <waypoint id='61'>
      <lat>29.758507</lat>
      <lon>-98.088057</lon>
      <ele>227.0</ele>
      <usgs>221.704101562</usgs>
    </waypoint>
    <waypoint id='62'>
      <lat>29.75906</lat>
      <lon>-98.087611</lon>
      <ele>227.0</ele>
      <usgs>223.992935181</usgs>
    </waypoint>
    <waypoint id='63'>
      <lat>29.759603</lat>
      <lon>-98.08718</lon>
      <ele>228.0</ele>
      <usgs>224.050338745</usgs>
    </waypoint>
    <waypoint id='64'>
      <lat>29.759882</lat>
      <lon>-98.086957</lon>
      <ele>228.0</ele>
      <usgs>224.060089111</usgs>
    </waypoint>
    <waypoint id='65'>
      <lat>29.760476</lat>
      <lon>-98.086444</lon>
      <ele>228.9</ele>
      <usgs>224.14175415</usgs>
    </waypoint>
    <waypoint id='66'>
      <lat>29.760513</lat>
      <lon>-98.086395</lon>
      <ele>228.9</ele>
      <usgs>224.14175415</usgs>
    </waypoint>
    <waypoint id='67'>
      <lat>29.760656</lat>
      <lon>-98.08604</lon>
      <ele>229.4</ele>
      <usgs>224.286087036</usgs>
    </waypoint>
    <waypoint id='68'>
      <lat>29.760838</lat>
      <lon>-98.085208</lon>
      <ele>229.4</ele>
      <usgs>225.674316406</usgs>
    </waypoint>
    <waypoint id='69'>
      <lat>29.761052</lat>
      <lon>-98.084262</lon>
      <ele>229.9</ele>
      <usgs>226.356582642</usgs>
    </waypoint>
    <waypoint id='70'>
      <lat>29.761228</lat>
      <lon>-98.083507</lon>
      <ele>230.4</ele>
      <usgs>225.754547119</usgs>
    </waypoint>
    <waypoint id='71'>
      <lat>29.76137</lat>
      <lon>-98.08289</lon>
      <ele>230.4</ele>
      <usgs>225.334960938</usgs>
    </waypoint>
    <waypoint id='72'>
      <lat>29.761541</lat>
      <lon>-98.082449</lon>
      <ele>229.4</ele>
      <usgs>224.150939941</usgs>
    </waypoint>
    <waypoint id='73'>
      <lat>29.761815</lat>
      <lon>-98.08209</lon>
      <ele>228.9</ele>
      <usgs>223.478149414</usgs>
    </waypoint>
    <waypoint id='74'>
      <lat>29.762339</lat>
      <lon>-98.081508</lon>
      <ele>229.4</ele>
      <usgs>223.367767334</usgs>
    </waypoint>
    <waypoint id='75'>
      <lat>29.762831</lat>
      <lon>-98.080957</lon>
      <ele>229.4</ele>
      <usgs>224.363510132</usgs>
    </waypoint>
    <waypoint id='76'>
      <lat>29.763418</lat>
      <lon>-98.080301</lon>
      <ele>229.4</ele>
      <usgs>225.136184692</usgs>
    </waypoint>
    <waypoint id='77'>
      <lat>29.763973</lat>
      <lon>-98.079679</lon>
      <ele>228.5</ele>
      <usgs>222.060195923</usgs>
    </waypoint>
    <waypoint id='78'>
      <lat>29.764311</lat>
      <lon>-98.079301</lon>
      <ele>225.6</ele>
      <usgs>220.66885376</usgs>
    </waypoint>
    <waypoint id='79'>
      <lat>29.764947</lat>
      <lon>-98.078623</lon>
      <ele>223.6</ele>
      <usgs>218.318618774</usgs>
    </waypoint>
    <waypoint id='80'>
      <lat>29.76559</lat>
      <lon>-98.077945</lon>
      <ele>220.8</ele>
      <usgs>214.351791382</usgs>
    </waypoint>
    <waypoint id='81'>
      <lat>29.76621</lat>
      <lon>-98.07731</lon>
      <ele>218.4</ele>
      <usgs>212.700317383</usgs>
    </waypoint>
    <waypoint id='82'>
      <lat>29.766673</lat>
      <lon>-98.076828</lon>
      <ele>217.9</ele>
      <usgs>211.952468872</usgs>
    </waypoint>
    <waypoint id='83'>
      <lat>29.76672</lat>
      <lon>-98.076769</lon>
      <ele>217.4</ele>
      <usgs>211.952468872</usgs>
    </waypoint>
    <waypoint id='84'>
      <lat>29.766832</lat>
      <lon>-98.076446</lon>
      <ele>216.4</ele>
      <usgs>212.189956665</usgs>
    </waypoint>
    <waypoint id='85'>
      <lat>29.766814</lat>
      <lon>-98.076291</lon>
      <ele>216.4</ele>
      <usgs>212.295227051</usgs>
    </waypoint>
    <waypoint id='86'>
      <lat>29.766776</lat>
      <lon>-98.07616</lon>
      <ele>216.0</ele>
      <usgs>212.328826904</usgs>
    </waypoint>
  </segment>

  <turn id='3'>
    <fromto>Hunter Rd. to FM 1102</fromto>
    <cue>LEFT onto FM 1102</cue>
    <comments>Hunter Rd. dead-ends into FM 1102.</comments>
  </turn>

  <segment id='4'>
    <road>FM 1102</road>
    <fromto>Hunter Rd. to Conrads Ln.</fromto>
    <comments>This is a short jog from Hunter Rd. to Conrads Ln.  Watch out for
      cross traffic.</comments>
    <lanes>2</lanes>
    <shoulder>1</shoulder>
    <traffic>Moderate</traffic>
    <speed>55</speed>
    <waypoint id='87'>
      <lat>29.766841</lat>
      <lon>-98.075974</lon>
      <ele>216.4</ele>
      <usgs>212.445388794</usgs>
    </waypoint>
    <waypoint id='88'>
      <lat>29.766934</lat>
      <lon>-98.075914</lon>
      <ele>216.4</ele>
      <usgs>212.480056763</usgs>
    </waypoint>
    <waypoint id='89'>
      <lat>29.767134</lat>
      <lon>-98.075817</lon>
      <ele>215.5</ele>
      <usgs>212.504135132</usgs>
    </waypoint>
  </segment>

  <turn id='4'>
    <fromto>FM 1102 to Conrads Ln.</fromto>
    <cue>RIGHT onto Conrads Ln.</cue>
    <comments>There is no sign, but its the first right.  This is almost
      immediate after turning onto FM 1102.</comments>
  </turn>

  <segment id='5'>
    <road>Conrads Ln.</road>
    <fromto>FM 1102 to Conrads Ln.</fromto>
    <comments>This road takes you behind a housing development and past the
      mysterious, fenced-off building with the satelite dishes.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='90'>
      <lat>29.76724</lat>
      <lon>-98.075696</lon>
      <ele>216.0</ele>
      <usgs>212.571273804</usgs>
    </waypoint>
    <waypoint id='91'>
      <lat>29.767202</lat>
      <lon>-98.07558</lon>
      <ele>216.0</ele>
      <usgs>212.689544678</usgs>
    </waypoint>
    <waypoint id='92'>
      <lat>29.767158</lat>
      <lon>-98.07553</lon>
      <ele>216.0</ele>
      <usgs>212.791000366</usgs>
    </waypoint>
    <waypoint id='93'>
      <lat>29.766691</lat>
      <lon>-98.075102</lon>
      <ele>216.4</ele>
      <usgs>213.365524292</usgs>
    </waypoint>
    <waypoint id='94'>
      <lat>29.766412</lat>
      <lon>-98.07484</lon>
      <ele>217.9</ele>
      <usgs>213.905426025</usgs>
    </waypoint>
    <waypoint id='95'>
      <lat>29.766237</lat>
      <lon>-98.074673</lon>
      <ele>219.3</ele>
      <usgs>214.211334229</usgs>
    </waypoint>
    <waypoint id='96'>
      <lat>29.766091</lat>
      <lon>-98.074511</lon>
      <ele>219.3</ele>
      <usgs>214.382278442</usgs>
    </waypoint>
    <waypoint id='97'>
      <lat>29.76592</lat>
      <lon>-98.074314</lon>
      <ele>220.8</ele>
      <usgs>214.424606323</usgs>
    </waypoint>
    <waypoint id='98'>
      <lat>29.765858</lat>
      <lon>-98.074273</lon>
      <ele>220.8</ele>
      <usgs>214.424606323</usgs>
    </waypoint>
    <waypoint id='99'>
      <lat>29.765721</lat>
      <lon>-98.074106</lon>
      <ele>218.8</ele>
      <usgs>214.500061035</usgs>
    </waypoint>
    <waypoint id='100'>
      <lat>29.765465</lat>
      <lon>-98.073812</lon>
      <ele>218.8</ele>
      <usgs>214.660903931</usgs>
    </waypoint>
    <waypoint id='101'>
      <lat>29.765203</lat>
      <lon>-98.07354</lon>
      <ele>218.8</ele>
      <usgs>214.533630371</usgs>
    </waypoint>
    <waypoint id='102'>
      <lat>29.764859</lat>
      <lon>-98.073163</lon>
      <ele>219.3</ele>
      <usgs>214.228866577</usgs>
    </waypoint>
    <waypoint id='103'>
      <lat>29.764347</lat>
      <lon>-98.072594</lon>
      <ele>218.4</ele>
      <usgs>214.648269653</usgs>
    </waypoint>
    <waypoint id='104'>
      <lat>29.763909</lat>
      <lon>-98.072112</lon>
      <ele>219.3</ele>
      <usgs>214.801940918</usgs>
    </waypoint>
    <waypoint id='105'>
      <lat>29.763454</lat>
      <lon>-98.071614</lon>
      <ele>220.3</ele>
      <usgs>216.475265503</usgs>
    </waypoint>
    <waypoint id='106'>
      <lat>29.763105</lat>
      <lon>-98.071224</lon>
      <ele>220.8</ele>
      <usgs>217.951293945</usgs>
    </waypoint>
    <waypoint id='107'>
      <lat>29.762735</lat>
      <lon>-98.070824</lon>
      <ele>222.7</ele>
      <usgs>221.110534668</usgs>
    </waypoint>
    <waypoint id='108'>
      <lat>29.762668</lat>
      <lon>-98.07075</lon>
      <ele>223.6</ele>
      <usgs>221.033554077</usgs>
    </waypoint>
    <waypoint id='109'>
      <lat>29.762357</lat>
      <lon>-98.070406</lon>
      <ele>224.6</ele>
      <usgs>223.139663696</usgs>
    </waypoint>
    <waypoint id='110'>
      <lat>29.762057</lat>
      <lon>-98.070077</lon>
      <ele>226.5</ele>
      <usgs>224.444885254</usgs>
    </waypoint>
    <waypoint id='111'>
      <lat>29.761632</lat>
      <lon>-98.069589</lon>
      <ele>227.0</ele>
      <usgs>224.607452393</usgs>
    </waypoint>
    <waypoint id='112'>
      <lat>29.76133</lat>
      <lon>-98.069228</lon>
      <ele>227.0</ele>
      <usgs>224.344146729</usgs>
    </waypoint>
    <waypoint id='113'>
      <lat>29.760948</lat>
      <lon>-98.068777</lon>
      <ele>227.0</ele>
      <usgs>223.734161377</usgs>
    </waypoint>
    <waypoint id='114'>
      <lat>29.760458</lat>
      <lon>-98.068199</lon>
      <ele>227.0</ele>
      <usgs>222.767715454</usgs>
    </waypoint>
    <waypoint id='115'>
      <lat>29.75996</lat>
      <lon>-98.067616</lon>
      <ele>226.5</ele>
      <usgs>222.190338135</usgs>
    </waypoint>
    <waypoint id='116'>
      <lat>29.759468</lat>
      <lon>-98.06703</lon>
      <ele>225.6</ele>
      <usgs>221.338027954</usgs>
    </waypoint>
    <waypoint id='117'>
      <lat>29.759007</lat>
      <lon>-98.066497</lon>
      <ele>223.2</ele>
      <usgs>220.107208252</usgs>
    </waypoint>
    <waypoint id='118'>
      <lat>29.758431</lat>
      <lon>-98.065814</lon>
      <ele>222.2</ele>
      <usgs>218.416015625</usgs>
    </waypoint>
    <waypoint id='119'>
      <lat>29.758019</lat>
      <lon>-98.065325</lon>
      <ele>220.3</ele>
      <usgs>217.100921631</usgs>
    </waypoint>
    <waypoint id='120'>
      <lat>29.757459</lat>
      <lon>-98.064678</lon>
      <ele>218.4</ele>
      <usgs>214.791946411</usgs>
    </waypoint>
    <waypoint id='121'>
      <lat>29.757269</lat>
      <lon>-98.064636</lon>
      <ele>218.8</ele>
      <usgs>214.217987061</usgs>
    </waypoint>
    <waypoint id='122'>
      <lat>29.757148</lat>
      <lon>-98.064731</lon>
      <ele>218.8</ele>
      <usgs>214.09437561</usgs>
    </waypoint>
    <waypoint id='123'>
      <lat>29.756572</lat>
      <lon>-98.065409</lon>
      <ele>217.4</ele>
      <usgs>214.00553894</usgs>
    </waypoint>
    <waypoint id='124'>
      <lat>29.755934</lat>
      <lon>-98.066168</lon>
      <ele>217.4</ele>
      <usgs>213.543045044</usgs>
    </waypoint>
    <waypoint id='125'>
      <lat>29.75556</lat>
      <lon>-98.0666</lon>
      <ele>216.4</ele>
      <usgs>213.311248779</usgs>
    </waypoint>
  </segment>

  <turn id='5'>
    <fromto>Conrads Ln. to Conrads Ln.</fromto>
    <cue>LEFT onto Conrads Ln.</cue>
    <comments>Conrads Ln. T's in on the left.  If you keep going straight, the
      street name changes.  Yes, that's confusing.</comments>
  </turn>

  <segment id='6'>
    <road>Conrads Ln.</road>
    <fromto>Conrads Ln. to Kohlenberg Rd.</fromto>
    <comments>Go past more fields and another housing development.  No more
      mysterious facilities here.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='126'>
      <lat>29.755337</lat>
      <lon>-98.066703</lon>
      <ele>216.4</ele>
      <usgs>213.306259155</usgs>
    </waypoint>
    <waypoint id='127'>
      <lat>29.755164</lat>
      <lon>-98.066584</lon>
      <ele>216.0</ele>
      <usgs>213.223342896</usgs>
    </waypoint>
    <waypoint id='128'>
      <lat>29.754617</lat>
      <lon>-98.065957</lon>
      <ele>215.0</ele>
      <usgs>212.880935669</usgs>
    </waypoint>
    <waypoint id='129'>
      <lat>29.754191</lat>
      <lon>-98.065458</lon>
      <ele>215.0</ele>
      <usgs>212.842514038</usgs>
    </waypoint>
    <waypoint id='130'>
      <lat>29.753682</lat>
      <lon>-98.064871</lon>
      <ele>216.4</ele>
      <usgs>213.497070312</usgs>
    </waypoint>
    <waypoint id='131'>
      <lat>29.75316</lat>
      <lon>-98.064262</lon>
      <ele>216.9</ele>
      <usgs>213.855941772</usgs>
    </waypoint>
    <waypoint id='132'>
      <lat>29.752662</lat>
      <lon>-98.063682</lon>
      <ele>220.3</ele>
      <usgs>215.561828613</usgs>
    </waypoint>
    <waypoint id='133'>
      <lat>29.752084</lat>
      <lon>-98.063011</lon>
      <ele>221.7</ele>
      <usgs>217.988342285</usgs>
    </waypoint>
    <waypoint id='134'>
      <lat>29.751639</lat>
      <lon>-98.062499</lon>
      <ele>221.7</ele>
      <usgs>219.883331299</usgs>
    </waypoint>
    <waypoint id='135'>
      <lat>29.751175</lat>
      <lon>-98.061973</lon>
      <ele>222.7</ele>
      <usgs>221.461975098</usgs>
    </waypoint>
    <waypoint id='136'>
      <lat>29.750777</lat>
      <lon>-98.06152</lon>
      <ele>225.6</ele>
      <usgs>224.150344849</usgs>
    </waypoint>
    <waypoint id='137'>
      <lat>29.750416</lat>
      <lon>-98.061101</lon>
      <ele>228.0</ele>
      <usgs>226.844894409</usgs>
    </waypoint>
    <waypoint id='138'>
      <lat>29.750129</lat>
      <lon>-98.060759</lon>
      <ele>230.9</ele>
      <usgs>228.739303589</usgs>
    </waypoint>
    <waypoint id='139'>
      <lat>29.749883</lat>
      <lon>-98.060479</lon>
      <ele>231.8</ele>
      <usgs>230.101165771</usgs>
    </waypoint>
    <waypoint id='140'>
      <lat>29.749521</lat>
      <lon>-98.06007</lon>
      <ele>231.8</ele>
      <usgs>231.61882019</usgs>
    </waypoint>
    <waypoint id='141'>
      <lat>29.749343</lat>
      <lon>-98.059866</lon>
      <ele>232.8</ele>
      <usgs>232.128082275</usgs>
    </waypoint>
    <waypoint id='142'>
      <lat>29.748971</lat>
      <lon>-98.059436</lon>
      <ele>234.7</ele>
      <usgs>233.70098877</usgs>
    </waypoint>
  </segment>

  <turn id='6'>
    <fromto>Conrads Ln. to highway overpass</fromto>
    <cue>RIGHT onto overpass</cue>
    <comments>Veer right at the Y intersection and take the bridge over the
      highway.</comments>
  </turn>

  <segment id='7'>
    <road>Highway Overpass</road>
    <fromto>Conrads Ln. to Kohlenberg Rd.</fromto>
    <comments>This is one of those weird things the highway department came-up
      with to confuse people.  Basically, you head straight over the highway
      and keep going the same direction you were already going in.</comments>
    <lanes>2</lanes>
    <shoulder>1</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='143' stop='1'>
      <lat>29.748665</lat>
      <lon>-98.059147</lon>
      <ele>234.7</ele>
      <usgs>233.716644287</usgs>
    </waypoint>
    <waypoint id='144'>
      <lat>29.748317</lat>
      <lon>-98.058961</lon>
      <ele>234.7</ele>
      <usgs>233.63432312</usgs>
    </waypoint>
    <waypoint id='145'>
      <lat>29.747907</lat>
      <lon>-98.058857</lon>
      <ele>234.7</ele>
      <usgs>233.532775879</usgs>
    </waypoint>
    <waypoint id='146'>
      <lat>29.747472</lat>
      <lon>-98.058796</lon>
      <ele>236.6</ele>
      <usgs>233.279312134</usgs>
    </waypoint>
    <waypoint id='147'>
      <lat>29.747378</lat>
      <lon>-98.058757</lon>
      <ele>238.1</ele>
      <usgs>233.257614136</usgs>
    </waypoint>
    <waypoint id='148'>
      <lat>29.747197</lat>
      <lon>-98.058579</lon>
      <ele>239.0</ele>
      <usgs>233.22076416</usgs>
    </waypoint>
    <waypoint id='149'>
      <lat>29.746928</lat>
      <lon>-98.058076</lon>
      <ele>240.9</ele>
      <usgs>233.136322021</usgs>
    </waypoint>
    <waypoint id='150'>
      <lat>29.746691</lat>
      <lon>-98.057643</lon>
      <ele>241.4</ele>
      <usgs>232.948699951</usgs>
    </waypoint>
    <waypoint id='151'>
      <lat>29.746486</lat>
      <lon>-98.057258</lon>
      <ele>239.0</ele>
      <usgs>233.023529053</usgs>
    </waypoint>
    <waypoint id='152'>
      <lat>29.746256</lat>
      <lon>-98.05703</lon>
      <ele>237.6</ele>
      <usgs>232.590393066</usgs>
    </waypoint>
    <waypoint id='153'>
      <lat>29.746179</lat>
      <lon>-98.057006</lon>
      <ele>237.1</ele>
      <usgs>232.299499512</usgs>
    </waypoint>
    <waypoint id='154'>
      <lat>29.745835</lat>
      <lon>-98.056943</lon>
      <ele>235.7</ele>
      <usgs>231.441635132</usgs>
    </waypoint>
    <waypoint id='155'>
      <lat>29.745547</lat>
      <lon>-98.056881</lon>
      <ele>233.7</ele>
      <usgs>229.58631897</usgs>
    </waypoint>
    <waypoint id='156'>
      <lat>29.74526</lat>
      <lon>-98.056777</lon>
      <ele>230.9</ele>
      <usgs>228.092376709</usgs>
    </waypoint>
  </segment>

  <turn id='7'>
    <fromto>Highway Overpass to Kohlenberg Rd.</fromto>
    <cue>LEFT onto Kohlenberg Rd.</cue>
    <comments>Bear left after crossing the highway and get onto Kohlenberg
      Rd.</comments>
  </turn>

  <segment id='8'>
    <road>Kohlenberg Rd.</road>
    <fromto>Hightway Overpass to FM 1101</fromto>
    <comments>Fields to the left, fields to the right.  Stuck in the middle
      again.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='157'>
      <lat>29.745072</lat>
      <lon>-98.056687</lon>
      <ele>229.9</ele>
      <usgs>227.318267822</usgs>
    </waypoint>
    <waypoint id='158'>
      <lat>29.744746</lat>
      <lon>-98.056446</lon>
      <ele>229.4</ele>
      <usgs>225.733657837</usgs>
    </waypoint>
    <waypoint id='159'>
      <lat>29.744371</lat>
      <lon>-98.056038</lon>
      <ele>228.5</ele>
      <usgs>224.272323608</usgs>
    </waypoint>
    <waypoint id='160'>
      <lat>29.74363</lat>
      <lon>-98.055203</lon>
      <ele>227.5</ele>
      <usgs>221.616790771</usgs>
    </waypoint>
    <waypoint id='161'>
      <lat>29.74293</lat>
      <lon>-98.054417</lon>
      <ele>225.1</ele>
      <usgs>220.735412598</usgs>
    </waypoint>
    <waypoint id='162'>
      <lat>29.742392</lat>
      <lon>-98.053809</lon>
      <ele>223.6</ele>
      <usgs>218.585357666</usgs>
    </waypoint>
    <waypoint id='163'>
      <lat>29.741724</lat>
      <lon>-98.053058</lon>
      <ele>220.3</ele>
      <usgs>217.071578979</usgs>
    </waypoint>
    <waypoint id='164'>
      <lat>29.741349</lat>
      <lon>-98.052637</lon>
      <ele>218.8</ele>
      <usgs>215.522079468</usgs>
    </waypoint>
    <waypoint id='165'>
      <lat>29.740566</lat>
      <lon>-98.051763</lon>
      <ele>216.4</ele>
      <usgs>211.259338379</usgs>
    </waypoint>
    <waypoint id='166'>
      <lat>29.740501</lat>
      <lon>-98.05169</lon>
      <ele>216.4</ele>
      <usgs>211.121871948</usgs>
    </waypoint>
    <waypoint id='167'>
      <lat>29.74008</lat>
      <lon>-98.051232</lon>
      <ele>215.5</ele>
      <usgs>212.947601318</usgs>
    </waypoint>
    <waypoint id='168'>
      <lat>29.739934</lat>
      <lon>-98.05107</lon>
      <ele>217.4</ele>
      <usgs>215.021560669</usgs>
    </waypoint>
    <waypoint id='169'>
      <lat>29.739645</lat>
      <lon>-98.050747</lon>
      <ele>218.8</ele>
      <usgs>216.01739502</usgs>
    </waypoint>
    <waypoint id='170'>
      <lat>29.739608</lat>
      <lon>-98.050706</lon>
      <ele>218.8</ele>
      <usgs>216.180389404</usgs>
    </waypoint>
    <waypoint id='171'>
      <lat>29.739272</lat>
      <lon>-98.050331</lon>
      <ele>218.8</ele>
      <usgs>216.135910034</usgs>
    </waypoint>
    <waypoint id='172'>
      <lat>29.738859</lat>
      <lon>-98.049871</lon>
      <ele>216.9</ele>
      <usgs>213.385284424</usgs>
    </waypoint>
    <waypoint id='173'>
      <lat>29.738247</lat>
      <lon>-98.049188</lon>
      <ele>216.0</ele>
      <usgs>212.171539307</usgs>
    </waypoint>
    <waypoint id='174'>
      <lat>29.737718</lat>
      <lon>-98.048601</lon>
      <ele>213.1</ele>
      <usgs>210.984161377</usgs>
    </waypoint>
    <waypoint id='175'>
      <lat>29.737388</lat>
      <lon>-98.048243</lon>
      <ele>211.6</ele>
      <usgs>209.994430542</usgs>
    </waypoint>
  </segment>

  <turn id='8'>
    <fromto>Kohlenberg Rd. to FM 1101</fromto>
    <cue>LEFT onto FM 1101</cue>
    <comments>Kohnlenberg Rd. dead-ends into FM 1101.</comments>
  </turn>

  <segment id='9'>
    <road>FM 1101</road>
    <fromto>Kohlenberg Rd. to Francis Harris Ln.</fromto>
    <comments>This road takes you past farms and the local landfill.  The
      landfill is poorly disguised as a hill, but it's too symetrical and is
      covered in contraptions to let the gases out of the fill.  You'll know
      instantly it's man-made.  Otherwise, this is a really pretty
      road. </comments>
    <lanes>2</lanes>
    <shoulder>1/4</shoulder>
    <traffic>Light</traffic>
    <speed>55</speed>
    <waypoint id='176'>
      <lat>29.737293</lat>
      <lon>-98.048116</lon>
      <ele>210.7</ele>
      <usgs>209.200485229</usgs>
    </waypoint>
    <waypoint id='177'>
      <lat>29.737344</lat>
      <lon>-98.047916</lon>
      <ele>210.2</ele>
      <usgs>209.027999878</usgs>
    </waypoint>
    <waypoint id='178'>
      <lat>29.737644</lat>
      <lon>-98.047431</lon>
      <ele>210.7</ele>
      <usgs>208.213012695</usgs>
    </waypoint>
    <waypoint id='179'>
      <lat>29.738057</lat>
      <lon>-98.04666</lon>
      <ele>210.7</ele>
      <usgs>208.783126831</usgs>
    </waypoint>
    <waypoint id='180'>
      <lat>29.738469</lat>
      <lon>-98.045872</lon>
      <ele>211.1</ele>
      <usgs>209.446304321</usgs>
    </waypoint>
    <waypoint id='181'>
      <lat>29.738938</lat>
      <lon>-98.044983</lon>
      <ele>212.1</ele>
      <usgs>208.227127075</usgs>
    </waypoint>
    <waypoint id='182'>
      <lat>29.73939</lat>
      <lon>-98.044121</lon>
      <ele>212.6</ele>
      <usgs>209.726074219</usgs>
    </waypoint>
    <waypoint id='183'>
      <lat>29.739736</lat>
      <lon>-98.043458</lon>
      <ele>213.6</ele>
      <usgs>211.62487793</usgs>
    </waypoint>
    <waypoint id='184'>
      <lat>29.740155</lat>
      <lon>-98.042654</lon>
      <ele>214.0</ele>
      <usgs>212.215530396</usgs>
    </waypoint>
    <waypoint id='185'>
      <lat>29.740511</lat>
      <lon>-98.041967</lon>
      <ele>213.6</ele>
      <usgs>211.906738281</usgs>
    </waypoint>
    <waypoint id='186'>
      <lat>29.740843</lat>
      <lon>-98.041318</lon>
      <ele>212.1</ele>
      <usgs>208.646484375</usgs>
    </waypoint>
    <waypoint id='187'>
      <lat>29.741181</lat>
      <lon>-98.040539</lon>
      <ele>209.2</ele>
      <usgs>204.348175049</usgs>
    </waypoint>
    <waypoint id='188'>
      <lat>29.741259</lat>
      <lon>-98.040324</lon>
      <ele>208.3</ele>
      <usgs>203.887924194</usgs>
    </waypoint>
    <waypoint id='189'>
      <lat>29.741513</lat>
      <lon>-98.039535</lon>
      <ele>206.3</ele>
      <usgs>200.863998413</usgs>
    </waypoint>
    <waypoint id='190'>
      <lat>29.741583</lat>
      <lon>-98.039304</lon>
      <ele>204.9</ele>
      <usgs>200.530731201</usgs>
    </waypoint>
    <waypoint id='191'>
      <lat>29.741655</lat>
      <lon>-98.039071</lon>
      <ele>203.9</ele>
      <usgs>199.570007324</usgs>
    </waypoint>
    <waypoint id='192'>
      <lat>29.742015</lat>
      <lon>-98.037929</lon>
      <ele>201.1</ele>
      <usgs>195.326705933</usgs>
    </waypoint>
    <waypoint id='193'>
      <lat>29.742239</lat>
      <lon>-98.037207</lon>
      <ele>201.5</ele>
      <usgs>197.355575562</usgs>
    </waypoint>
    <waypoint id='194'>
      <lat>29.742401</lat>
      <lon>-98.036678</lon>
      <ele>201.5</ele>
      <usgs>199.362213135</usgs>
    </waypoint>
    <waypoint id='195'>
      <lat>29.742535</lat>
      <lon>-98.036145</lon>
      <ele>202.5</ele>
      <usgs>201.445877075</usgs>
    </waypoint>
    <waypoint id='196'>
      <lat>29.742646</lat>
      <lon>-98.035458</lon>
      <ele>204.4</ele>
      <usgs>203.39932251</usgs>
    </waypoint>
    <waypoint id='197'>
      <lat>29.742701</lat>
      <lon>-98.034735</lon>
      <ele>204.9</ele>
      <usgs>204.646057129</usgs>
    </waypoint>
    <waypoint id='198'>
      <lat>29.742716</lat>
      <lon>-98.033997</lon>
      <ele>204.4</ele>
      <usgs>204.322891235</usgs>
    </waypoint>
    <waypoint id='199'>
      <lat>29.742727</lat>
      <lon>-98.033313</lon>
      <ele>203.0</ele>
      <usgs>198.423721313</usgs>
    </waypoint>
    <waypoint id='200'>
      <lat>29.742745</lat>
      <lon>-98.032397</lon>
      <ele>200.1</ele>
      <usgs>193.166320801</usgs>
    </waypoint>
    <waypoint id='201'>
      <lat>29.742758</lat>
      <lon>-98.031546</lon>
      <ele>199.1</ele>
      <usgs>194.351837158</usgs>
    </waypoint>
    <waypoint id='202'>
      <lat>29.742767</lat>
      <lon>-98.031012</lon>
      <ele>199.6</ele>
      <usgs>197.188018799</usgs>
    </waypoint>
    <waypoint id='203'>
      <lat>29.742776</lat>
      <lon>-98.030493</lon>
      <ele>200.6</ele>
      <usgs>199.075210571</usgs>
    </waypoint>
    <waypoint id='204' poi='1'>
      <lat>29.742777</lat>
      <lon>-98.03002</lon>
      <ele>203.0</ele>
      <usgs>200.794021606</usgs>
    </waypoint>
    <waypoint id='205'>
      <lat>29.742787</lat>
      <lon>-98.029377</lon>
      <ele>204.4</ele>
      <usgs>203.197235107</usgs>
    </waypoint>
    <waypoint id='206'>
      <lat>29.742802</lat>
      <lon>-98.028651</lon>
      <ele>206.3</ele>
      <usgs>204.392547607</usgs>
    </waypoint>
    <waypoint id='207'>
      <lat>29.742822</lat>
      <lon>-98.027892</lon>
      <ele>207.3</ele>
      <usgs>204.68812561</usgs>
    </waypoint>
    <waypoint id='208'>
      <lat>29.742847</lat>
      <lon>-98.027044</lon>
      <ele>206.3</ele>
      <usgs>203.386245728</usgs>
    </waypoint>
    <waypoint id='209'>
      <lat>29.742863</lat>
      <lon>-98.026247</lon>
      <ele>205.4</ele>
      <usgs>200.699707031</usgs>
    </waypoint>
    <waypoint id='210'>
      <lat>29.742874</lat>
      <lon>-98.02567</lon>
      <ele>203.5</ele>
      <usgs>199.759918213</usgs>
    </waypoint>
    <waypoint id='211'>
      <lat>29.742922</lat>
      <lon>-98.024666</lon>
      <ele>202.0</ele>
      <usgs>195.321762085</usgs>
    </waypoint>
    <waypoint id='212'>
      <lat>29.743023</lat>
      <lon>-98.023801</lon>
      <ele>201.1</ele>
      <usgs>197.119873047</usgs>
    </waypoint>
    <waypoint id='213'>
      <lat>29.743196</lat>
      <lon>-98.022869</lon>
      <ele>200.6</ele>
      <usgs>197.471984863</usgs>
    </waypoint>
    <waypoint id='214'>
      <lat>29.743427</lat>
      <lon>-98.021986</lon>
      <ele>201.5</ele>
      <usgs>198.198898315</usgs>
    </waypoint>
    <waypoint id='215'>
      <lat>29.743697</lat>
      <lon>-98.021175</lon>
      <ele>200.6</ele>
      <usgs>195.346725464</usgs>
    </waypoint>
    <waypoint id='216'>
      <lat>29.743881</lat>
      <lon>-98.020699</lon>
      <ele>198.6</ele>
      <usgs>194.381240845</usgs>
    </waypoint>
    <waypoint id='217'>
      <lat>29.744086</lat>
      <lon>-98.020222</lon>
      <ele>197.7</ele>
      <usgs>194.179122925</usgs>
    </waypoint>
    <waypoint id='218'>
      <lat>29.744472</lat>
      <lon>-98.019451</lon>
      <ele>198.2</ele>
      <usgs>194.585189819</usgs>
    </waypoint>
    <waypoint id='219'>
      <lat>29.744938</lat>
      <lon>-98.018666</lon>
      <ele>197.2</ele>
      <usgs>194.299163818</usgs>
    </waypoint>
    <waypoint id='220'>
      <lat>29.745392</lat>
      <lon>-98.018023</lon>
      <ele>195.8</ele>
      <usgs>191.575363159</usgs>
    </waypoint>
    <waypoint id='221'>
      <lat>29.745715</lat>
      <lon>-98.017615</lon>
      <ele>194.8</ele>
      <usgs>190.952819824</usgs>
    </waypoint>
    <waypoint id='222'>
      <lat>29.74626</lat>
      <lon>-98.016976</lon>
      <ele>192.4</ele>
      <usgs>188.649368286</usgs>
    </waypoint>
    <waypoint id='223'>
      <lat>29.746873</lat>
      <lon>-98.016247</lon>
      <ele>191.0</ele>
      <usgs>185.390548706</usgs>
    </waypoint>
    <waypoint id='224'>
      <lat>29.747585</lat>
      <lon>-98.015378</lon>
      <ele>189.0</ele>
      <usgs>183.193130493</usgs>
    </waypoint>
    <waypoint id='225'>
      <lat>29.747722</lat>
      <lon>-98.015209</lon>
      <ele>188.1</ele>
      <usgs>182.661712646</usgs>
    </waypoint>
    <waypoint id='226'>
      <lat>29.748342</lat>
      <lon>-98.014452</lon>
      <ele>187.1</ele>
      <usgs>181.504806519</usgs>
    </waypoint>
    <waypoint id='227'>
      <lat>29.748943</lat>
      <lon>-98.013718</lon>
      <ele>185.7</ele>
      <usgs>180.122879028</usgs>
    </waypoint>
    <waypoint id='228'>
      <lat>29.749643</lat>
      <lon>-98.012864</lon>
      <ele>184.2</ele>
      <usgs>179.718719482</usgs>
    </waypoint>
    <waypoint id='229'>
      <lat>29.750405</lat>
      <lon>-98.011931</lon>
      <ele>182.8</ele>
      <usgs>180.770385742</usgs>
    </waypoint>
    <waypoint id='230'>
      <lat>29.750922</lat>
      <lon>-98.011292</lon>
      <ele>183.7</ele>
      <usgs>181.194702148</usgs>
    </waypoint>
    <waypoint id='231'>
      <lat>29.751087</lat>
      <lon>-98.011093</lon>
      <ele>185.2</ele>
      <usgs>181.570785522</usgs>
    </waypoint>
    <waypoint id='232'>
      <lat>29.751546</lat>
      <lon>-98.010534</lon>
      <ele>186.2</ele>
      <usgs>182.951187134</usgs>
    </waypoint>
    <waypoint id='233'>
      <lat>29.751642</lat>
      <lon>-98.010415</lon>
      <ele>187.1</ele>
      <usgs>183.008346558</usgs>
    </waypoint>
    <waypoint id='234'>
      <lat>29.752277</lat>
      <lon>-98.009638</lon>
      <ele>188.1</ele>
      <usgs>185.542602539</usgs>
    </waypoint>
    <waypoint id='235'>
      <lat>29.752793</lat>
      <lon>-98.008997</lon>
      <ele>190.0</ele>
      <usgs>187.084945679</usgs>
    </waypoint>
    <waypoint id='236'>
      <lat>29.753134</lat>
      <lon>-98.008481</lon>
      <ele>190.5</ele>
      <usgs>187.969619751</usgs>
    </waypoint>
    <waypoint id='237'>
      <lat>29.753404</lat>
      <lon>-98.007923</lon>
      <ele>190.5</ele>
      <usgs>188.989761353</usgs>
    </waypoint>
    <waypoint id='238'>
      <lat>29.753608</lat>
      <lon>-98.007287</lon>
      <ele>192.9</ele>
      <usgs>190.289489746</usgs>
    </waypoint>
    <waypoint id='239'>
      <lat>29.753727</lat>
      <lon>-98.006638</lon>
      <ele>194.3</ele>
      <usgs>191.212432861</usgs>
    </waypoint>
    <waypoint id='240'>
      <lat>29.75376</lat>
      <lon>-98.006051</lon>
      <ele>193.8</ele>
      <usgs>190.5234375</usgs>
    </waypoint>
    <waypoint id='241'>
      <lat>29.753728</lat>
      <lon>-98.005499</lon>
      <ele>192.9</ele>
      <usgs>189.211074829</usgs>
    </waypoint>
    <waypoint id='242'>
      <lat>29.753641</lat>
      <lon>-98.00496</lon>
      <ele>191.9</ele>
      <usgs>187.840744019</usgs>
    </waypoint>
    <waypoint id='243'>
      <lat>29.753597</lat>
      <lon>-98.004775</lon>
      <ele>191.4</ele>
      <usgs>187.327468872</usgs>
    </waypoint>
    <waypoint id='244'>
      <lat>29.753417</lat>
      <lon>-98.004217</lon>
      <ele>189.0</ele>
      <usgs>185.963287354</usgs>
    </waypoint>
    <waypoint id='245'>
      <lat>29.753109</lat>
      <lon>-98.003573</lon>
      <ele>188.1</ele>
      <usgs>184.230117798</usgs>
    </waypoint>
    <waypoint id='246'>
      <lat>29.752818</lat>
      <lon>-98.003118</lon>
      <ele>186.6</ele>
      <usgs>183.027984619</usgs>
    </waypoint>
    <waypoint id='247'>
      <lat>29.752779</lat>
      <lon>-98.003059</lon>
      <ele>185.2</ele>
      <usgs>183.027984619</usgs>
    </waypoint>
  </segment>

  <turn id='10'>
    <fromto>FM 1101 to Francis Harris Ln.</fromto>
    <cue>LEFT onto Francis Harris Ln.</cue>
    <comments>Francis Harris Ln. T's in on the left.</comments>
  </turn>

  <segment id='11'>
    <road>Francis Harris Ln.</road>
    <fromto>FM 1101 to York Creek Rd.</fromto>
    <comments>Go down the hill and across the creek.  You are still in the
      country.  It's easy to tell.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='679'>
      <lat>29.752716</lat>
      <lon>-98.002785</lon>
      <ele>180.9</ele>
      <usgs>182.229675293</usgs>
    </waypoint>
    <waypoint id='680'>
      <lat>29.752744</lat>
      <lon>-98.002752</lon>
      <ele>181.3</ele>
      <usgs>181.994613647</usgs>
    </waypoint>
    <waypoint id='681'>
      <lat>29.753051</lat>
      <lon>-98.002404</lon>
      <ele>179.9</ele>
      <usgs>181.417053223</usgs>
    </waypoint>
    <waypoint id='682'>
      <lat>29.753409</lat>
      <lon>-98.001991</lon>
      <ele>180.4</ele>
      <usgs>180.635803223</usgs>
    </waypoint>
    <waypoint id='683'>
      <lat>29.753964</lat>
      <lon>-98.001362</lon>
      <ele>178.5</ele>
      <usgs>179.004684448</usgs>
    </waypoint>
    <waypoint id='684'>
      <lat>29.754568</lat>
      <lon>-98.000701</lon>
      <ele>176.5</ele>
      <usgs>177.49546814</usgs>
    </waypoint>
    <waypoint id='685'>
      <lat>29.755203</lat>
      <lon>-98.000001</lon>
      <ele>175.1</ele>
      <usgs>174.120483398</usgs>
    </waypoint>
    <waypoint id='686'>
      <lat>29.755601</lat>
      <lon>-97.999558</lon>
      <ele>171.7</ele>
      <usgs>171.058517456</usgs>
    </waypoint>
    <waypoint id='687'>
      <lat>29.755897</lat>
      <lon>-97.999223</lon>
      <ele>168.8</ele>
      <usgs>168.385635376</usgs>
    </waypoint>
    <waypoint id='688'>
      <lat>29.755973</lat>
      <lon>-97.999138</lon>
      <ele>168.4</ele>
      <usgs>167.34815979</usgs>
    </waypoint>
    <waypoint id='689'>
      <lat>29.756404</lat>
      <lon>-97.998647</lon>
      <ele>165.0</ele>
      <usgs>164.626037598</usgs>
    </waypoint>
    <waypoint id='690'>
      <lat>29.756762</lat>
      <lon>-97.998241</lon>
      <ele>166.0</ele>
      <usgs>165.098632812</usgs>
    </waypoint>
    <waypoint id='691'>
      <lat>29.757216</lat>
      <lon>-97.99773</lon>
      <ele>165.5</ele>
      <usgs>166.130706787</usgs>
    </waypoint>
    <waypoint id='692'>
      <lat>29.757359</lat>
      <lon>-97.997572</lon>
      <ele>166.9</ele>
      <usgs>166.347137451</usgs>
    </waypoint>
    <waypoint id='693'>
      <lat>29.757827</lat>
      <lon>-97.997054</lon>
      <ele>166.0</ele>
      <usgs>166.58392334</usgs>
    </waypoint>
    <waypoint id='694'>
      <lat>29.758245</lat>
      <lon>-97.996586</lon>
      <ele>165.5</ele>
      <usgs>166.626083374</usgs>
    </waypoint>
    <waypoint id='695'>
      <lat>29.758761</lat>
      <lon>-97.996016</lon>
      <ele>165.5</ele>
      <usgs>166.439926147</usgs>
    </waypoint>
    <waypoint id='696'>
      <lat>29.759127</lat>
      <lon>-97.995608</lon>
      <ele>166.0</ele>
      <usgs>166.19329834</usgs>
    </waypoint>
    <waypoint id='697'>
      <lat>29.759628</lat>
      <lon>-97.99505</lon>
      <ele>165.0</ele>
      <usgs>165.288497925</usgs>
    </waypoint>
    <waypoint id='698'>
      <lat>29.759999</lat>
      <lon>-97.994591</lon>
      <ele>163.1</ele>
      <usgs>164.666046143</usgs>
    </waypoint>
    <waypoint id='699'>
      <lat>29.760333</lat>
      <lon>-97.994176</lon>
      <ele>165.0</ele>
      <usgs>164.698684692</usgs>
    </waypoint>
    <waypoint id='700'>
      <lat>29.760702</lat>
      <lon>-97.993751</lon>
      <ele>165.0</ele>
      <usgs>165.016662598</usgs>
    </waypoint>
  </segment>

  <turn id='11'>
    <fromto>Francis Harris Ln. to York Creek Rd.</fromto>
    <cue>LEFT onto York Creek Rd.</cue>
    <comments>York Creek Rd. T's in on the left.</comments>
  </turn>

  <segment id='12'>
    <road>York Creek Rd.</road>
    <fromto>Francis Harris Ln. to Old Bastrop Rd.</fromto>
    <comments>This is a cool road with a lot of tree tunnels (trees overhang
      the road from both sides).</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='701'>
      <lat>29.760872</lat>
      <lon>-97.993683</lon>
      <ele>165.5</ele>
      <usgs>165.149414062</usgs>
    </waypoint>
    <waypoint id='702'>
      <lat>29.760919</lat>
      <lon>-97.993705</lon>
      <ele>165.5</ele>
      <usgs>165.158630371</usgs>
    </waypoint>
    <waypoint id='703'>
      <lat>29.761419</lat>
      <lon>-97.993991</lon>
      <ele>165.5</ele>
      <usgs>165.352401733</usgs>
    </waypoint>
    <waypoint id='704'>
      <lat>29.761742</lat>
      <lon>-97.994165</lon>
      <ele>165.5</ele>
      <usgs>165.309463501</usgs>
    </waypoint>
    <waypoint id='705'>
      <lat>29.761981</lat>
      <lon>-97.994217</lon>
      <ele>165.5</ele>
      <usgs>165.302566528</usgs>
    </waypoint>
    <waypoint id='706'>
      <lat>29.762424</lat>
      <lon>-97.994213</lon>
      <ele>164.5</ele>
      <usgs>165.757720947</usgs>
    </waypoint>
    <waypoint id='707'>
      <lat>29.762907</lat>
      <lon>-97.994192</lon>
      <ele>164.0</ele>
      <usgs>166.204421997</usgs>
    </waypoint>
    <waypoint id='708'>
      <lat>29.763434</lat>
      <lon>-97.994111</lon>
      <ele>165.0</ele>
      <usgs>166.543670654</usgs>
    </waypoint>
    <waypoint id='709'>
      <lat>29.763804</lat>
      <lon>-97.994054</lon>
      <ele>165.5</ele>
      <usgs>166.718566895</usgs>
    </waypoint>
    <waypoint id='710'>
      <lat>29.764294</lat>
      <lon>-97.993986</lon>
      <ele>166.0</ele>
      <usgs>166.846511841</usgs>
    </waypoint>
    <waypoint id='711'>
      <lat>29.76473</lat>
      <lon>-97.993955</lon>
      <ele>166.0</ele>
      <usgs>166.884552002</usgs>
    </waypoint>
    <waypoint id='712'>
      <lat>29.765157</lat>
      <lon>-97.994039</lon>
      <ele>166.9</ele>
      <usgs>166.890762329</usgs>
    </waypoint>
    <waypoint id='713'>
      <lat>29.765742</lat>
      <lon>-97.994279</lon>
      <ele>166.9</ele>
      <usgs>166.926956177</usgs>
    </waypoint>
    <waypoint id='714'>
      <lat>29.766271</lat>
      <lon>-97.994468</lon>
      <ele>166.9</ele>
      <usgs>166.927597046</usgs>
    </waypoint>
    <waypoint id='715'>
      <lat>29.766685</lat>
      <lon>-97.994584</lon>
      <ele>167.4</ele>
      <usgs>166.976348877</usgs>
    </waypoint>
    <waypoint id='716'>
      <lat>29.766865</lat>
      <lon>-97.994639</lon>
      <ele>167.4</ele>
      <usgs>167.006393433</usgs>
    </waypoint>
    <waypoint id='717'>
      <lat>29.767231</lat>
      <lon>-97.994729</lon>
      <ele>167.4</ele>
      <usgs>167.025314331</usgs>
    </waypoint>
    <waypoint id='718'>
      <lat>29.767544</lat>
      <lon>-97.994824</lon>
      <ele>167.9</ele>
      <usgs>167.04045105</usgs>
    </waypoint>
    <waypoint id='719'>
      <lat>29.767607</lat>
      <lon>-97.994843</lon>
      <ele>167.9</ele>
      <usgs>167.038497925</usgs>
    </waypoint>
    <waypoint id='720'>
      <lat>29.767723</lat>
      <lon>-97.994893</lon>
      <ele>167.4</ele>
      <usgs>167.027099609</usgs>
    </waypoint>
    <waypoint id='721'>
      <lat>29.767941</lat>
      <lon>-97.995143</lon>
      <ele>167.4</ele>
      <usgs>167.169342041</usgs>
    </waypoint>
    <waypoint id='722'>
      <lat>29.767969</lat>
      <lon>-97.995207</lon>
      <ele>167.9</ele>
      <usgs>167.22026062</usgs>
    </waypoint>
    <waypoint id='723'>
      <lat>29.768206</lat>
      <lon>-97.995869</lon>
      <ele>168.4</ele>
      <usgs>167.506912231</usgs>
    </waypoint>
    <waypoint id='724'>
      <lat>29.76843</lat>
      <lon>-97.996468</lon>
      <ele>168.4</ele>
      <usgs>167.585601807</usgs>
    </waypoint>
    <waypoint id='725'>
      <lat>29.768714</lat>
      <lon>-97.997222</lon>
      <ele>167.9</ele>
      <usgs>167.551895142</usgs>
    </waypoint>
    <waypoint id='726'>
      <lat>29.76878</lat>
      <lon>-97.997673</lon>
      <ele>168.4</ele>
      <usgs>167.603057861</usgs>
    </waypoint>
    <waypoint id='727'>
      <lat>29.768835</lat>
      <lon>-97.998347</lon>
      <ele>167.4</ele>
      <usgs>167.786956787</usgs>
    </waypoint>
    <waypoint id='728'>
      <lat>29.768898</lat>
      <lon>-97.998795</lon>
      <ele>167.9</ele>
      <usgs>167.946029663</usgs>
    </waypoint>
    <waypoint id='729'>
      <lat>29.768993</lat>
      <lon>-97.999269</lon>
      <ele>167.9</ele>
      <usgs>168.149124146</usgs>
    </waypoint>
    <waypoint id='730'>
      <lat>29.769129</lat>
      <lon>-97.999944</lon>
      <ele>169.3</ele>
      <usgs>168.460083008</usgs>
    </waypoint>
    <waypoint id='731'>
      <lat>29.76927</lat>
      <lon>-98.000658</lon>
      <ele>169.3</ele>
      <usgs>168.702255249</usgs>
    </waypoint>
    <waypoint id='732'>
      <lat>29.769406</lat>
      <lon>-98.001367</lon>
      <ele>169.3</ele>
      <usgs>168.949569702</usgs>
    </waypoint>
    <waypoint id='733'>
      <lat>29.769548</lat>
      <lon>-98.001843</lon>
      <ele>170.3</ele>
      <usgs>169.111968994</usgs>
    </waypoint>
    <waypoint id='734'>
      <lat>29.769781</lat>
      <lon>-98.002185</lon>
      <ele>169.3</ele>
      <usgs>169.272872925</usgs>
    </waypoint>
    <waypoint id='735'>
      <lat>29.770077</lat>
      <lon>-98.002672</lon>
      <ele>170.3</ele>
      <usgs>169.539779663</usgs>
    </waypoint>
    <waypoint id='736'>
      <lat>29.770303</lat>
      <lon>-98.00284</lon>
      <ele>169.8</ele>
      <usgs>169.789596558</usgs>
    </waypoint>
    <waypoint id='737'>
      <lat>29.770444</lat>
      <lon>-98.002863</lon>
      <ele>169.8</ele>
      <usgs>169.841003418</usgs>
    </waypoint>
    <waypoint id='738'>
      <lat>29.770871</lat>
      <lon>-98.002821</lon>
      <ele>169.8</ele>
      <usgs>170.025558472</usgs>
    </waypoint>
    <waypoint id='739'>
      <lat>29.771356</lat>
      <lon>-98.002757</lon>
      <ele>169.8</ele>
      <usgs>169.90586853</usgs>
    </waypoint>
    <waypoint id='740'>
      <lat>29.771737</lat>
      <lon>-98.002836</lon>
      <ele>169.8</ele>
      <usgs>170.16595459</usgs>
    </waypoint>
    <waypoint id='741'>
      <lat>29.772081</lat>
      <lon>-98.003046</lon>
      <ele>170.3</ele>
      <usgs>170.353302002</usgs>
    </waypoint>
    <waypoint id='742'>
      <lat>29.772738</lat>
      <lon>-98.003529</lon>
      <ele>169.8</ele>
      <usgs>170.704025269</usgs>
    </waypoint>
    <waypoint id='743'>
      <lat>29.773075</lat>
      <lon>-98.003834</lon>
      <ele>169.8</ele>
      <usgs>170.69519043</usgs>
    </waypoint>
    <waypoint id='744'>
      <lat>29.773559</lat>
      <lon>-98.004303</lon>
      <ele>169.8</ele>
      <usgs>170.635467529</usgs>
    </waypoint>
    <waypoint id='745'>
      <lat>29.773977</lat>
      <lon>-98.004606</lon>
      <ele>169.8</ele>
      <usgs>170.626937866</usgs>
    </waypoint>
    <waypoint id='746'>
      <lat>29.774398</lat>
      <lon>-98.004896</lon>
      <ele>169.8</ele>
      <usgs>170.581832886</usgs>
    </waypoint>
    <waypoint id='747'>
      <lat>29.774848</lat>
      <lon>-98.005212</lon>
      <ele>170.3</ele>
      <usgs>170.80859375</usgs>
    </waypoint>
    <waypoint id='748'>
      <lat>29.775289</lat>
      <lon>-98.005544</lon>
      <ele>171.7</ele>
      <usgs>170.886474609</usgs>
    </waypoint>
    <waypoint id='749'>
      <lat>29.775719</lat>
      <lon>-98.005907</lon>
      <ele>171.7</ele>
      <usgs>170.952774048</usgs>
    </waypoint>
    <waypoint id='750'>
      <lat>29.7762</lat>
      <lon>-98.006328</lon>
      <ele>172.2</ele>
      <usgs>170.975097656</usgs>
    </waypoint>
    <waypoint id='760'>
      <lat>29.776315</lat>
      <lon>-98.006389</lon>
      <ele>171.3</ele>
      <usgs>170.938552856</usgs>
    </waypoint>
    <waypoint id='761'>
      <lat>29.776385</lat>
      <lon>-98.006459</lon>
      <ele>171.7</ele>
      <usgs>170.938552856</usgs>
    </waypoint>
    <waypoint id='762'>
      <lat>29.776653</lat>
      <lon>-98.006724</lon>
      <ele>171.7</ele>
      <usgs>170.913726807</usgs>
    </waypoint>
    <waypoint id='763'>
      <lat>29.776882</lat>
      <lon>-98.00701</lon>
      <ele>172.2</ele>
      <usgs>170.896820068</usgs>
    </waypoint>
    <waypoint id='764'>
      <lat>29.777167</lat>
      <lon>-98.007456</lon>
      <ele>172.7</ele>
      <usgs>170.911346436</usgs>
    </waypoint>
    <waypoint id='765'>
      <lat>29.777487</lat>
      <lon>-98.007983</lon>
      <ele>173.2</ele>
      <usgs>171.152755737</usgs>
    </waypoint>
    <waypoint id='766'>
      <lat>29.777713</lat>
      <lon>-98.008294</lon>
      <ele>173.2</ele>
      <usgs>171.359863281</usgs>
    </waypoint>
    <waypoint id='767'>
      <lat>29.777977</lat>
      <lon>-98.008485</lon>
      <ele>173.2</ele>
      <usgs>171.560562134</usgs>
    </waypoint>
    <waypoint id='768'>
      <lat>29.77831</lat>
      <lon>-98.008578</lon>
      <ele>173.2</ele>
      <usgs>171.788497925</usgs>
    </waypoint>
    <waypoint id='769'>
      <lat>29.778854</lat>
      <lon>-98.008687</lon>
      <ele>172.2</ele>
      <usgs>172.230865479</usgs>
    </waypoint>
    <waypoint id='770'>
      <lat>29.779648</lat>
      <lon>-98.008846</lon>
      <ele>172.2</ele>
      <usgs>173.195236206</usgs>
    </waypoint>
    <waypoint id='771'>
      <lat>29.780135</lat>
      <lon>-98.008911</lon>
      <ele>171.7</ele>
      <usgs>173.816818237</usgs>
    </waypoint>
    <waypoint id='772'>
      <lat>29.780506</lat>
      <lon>-98.008861</lon>
      <ele>172.7</ele>
      <usgs>174.013381958</usgs>
    </waypoint>
    <waypoint id='773'>
      <lat>29.780856</lat>
      <lon>-98.008771</lon>
      <ele>172.2</ele>
      <usgs>173.993408203</usgs>
    </waypoint>
    <waypoint id='774'>
      <lat>29.78115</lat>
      <lon>-98.008816</lon>
      <ele>172.7</ele>
      <usgs>174.220657349</usgs>
    </waypoint>
    <waypoint id='775'>
      <lat>29.781308</lat>
      <lon>-98.008939</lon>
      <ele>173.2</ele>
      <usgs>174.446472168</usgs>
    </waypoint>
    <waypoint id='776'>
      <lat>29.781596</lat>
      <lon>-98.009293</lon>
      <ele>173.2</ele>
      <usgs>175.201385498</usgs>
    </waypoint>
    <waypoint id='777'>
      <lat>29.781801</lat>
      <lon>-98.009708</lon>
      <ele>173.7</ele>
      <usgs>175.653793335</usgs>
    </waypoint>
    <waypoint id='778'>
      <lat>29.781968</lat>
      <lon>-98.01027</lon>
      <ele>173.2</ele>
      <usgs>175.572723389</usgs>
    </waypoint>
    <waypoint id='779'>
      <lat>29.782075</lat>
      <lon>-98.010665</lon>
      <ele>174.1</ele>
      <usgs>175.637237549</usgs>
    </waypoint>
    <waypoint id='780'>
      <lat>29.782275</lat>
      <lon>-98.011181</lon>
      <ele>173.2</ele>
      <usgs>175.643554688</usgs>
    </waypoint>
    <waypoint id='781'>
      <lat>29.782543</lat>
      <lon>-98.011825</lon>
      <ele>174.6</ele>
      <usgs>175.982528687</usgs>
    </waypoint>
    <waypoint id='782'>
      <lat>29.782826</lat>
      <lon>-98.012294</lon>
      <ele>174.1</ele>
      <usgs>176.304428101</usgs>
    </waypoint>
    <waypoint id='783'>
      <lat>29.783108</lat>
      <lon>-98.012725</lon>
      <ele>175.1</ele>
      <usgs>176.818710327</usgs>
    </waypoint>
    <waypoint id='784'>
      <lat>29.783476</lat>
      <lon>-98.013259</lon>
      <ele>176.1</ele>
      <usgs>177.205612183</usgs>
    </waypoint>
    <waypoint id='785'>
      <lat>29.783788</lat>
      <lon>-98.013743</lon>
      <ele>177.0</ele>
      <usgs>177.253311157</usgs>
    </waypoint>
    <waypoint id='786'>
      <lat>29.784226</lat>
      <lon>-98.014405</lon>
      <ele>177.0</ele>
      <usgs>177.209243774</usgs>
    </waypoint>
    <waypoint id='787'>
      <lat>29.784566</lat>
      <lon>-98.014886</lon>
      <ele>177.5</ele>
      <usgs>177.29359436</usgs>
    </waypoint>
    <waypoint id='788'>
      <lat>29.785052</lat>
      <lon>-98.015517</lon>
      <ele>177.0</ele>
      <usgs>177.732025146</usgs>
    </waypoint>
    <waypoint id='789'>
      <lat>29.785358</lat>
      <lon>-98.015901</lon>
      <ele>177.0</ele>
      <usgs>177.924743652</usgs>
    </waypoint>
    <waypoint id='790'>
      <lat>29.785825</lat>
      <lon>-98.016493</lon>
      <ele>178.0</ele>
      <usgs>177.947875977</usgs>
    </waypoint>
    <waypoint id='791'>
      <lat>29.786234</lat>
      <lon>-98.017021</lon>
      <ele>178.5</ele>
      <usgs>177.690475464</usgs>
    </waypoint>
    <waypoint id='792'>
      <lat>29.786742</lat>
      <lon>-98.017679</lon>
      <ele>178.9</ele>
      <usgs>177.294754028</usgs>
    </waypoint>
    <waypoint id='793'>
      <lat>29.787241</lat>
      <lon>-98.018321</lon>
      <ele>178.5</ele>
      <usgs>177.187438965</usgs>
    </waypoint>
    <waypoint id='794'>
      <lat>29.787787</lat>
      <lon>-98.019033</lon>
      <ele>178.9</ele>
      <usgs>177.914535522</usgs>
    </waypoint>
    <waypoint id='795'>
      <lat>29.788294</lat>
      <lon>-98.019692</lon>
      <ele>179.4</ele>
      <usgs>178.765975952</usgs>
    </waypoint>
    <waypoint id='796'>
      <lat>29.788788</lat>
      <lon>-98.02034</lon>
      <ele>180.4</ele>
      <usgs>179.70375061</usgs>
    </waypoint>
    <waypoint id='797'>
      <lat>29.789285</lat>
      <lon>-98.02098</lon>
      <ele>180.9</ele>
      <usgs>181.096908569</usgs>
    </waypoint>
    <waypoint id='798'>
      <lat>29.789654</lat>
      <lon>-98.021424</lon>
      <ele>180.9</ele>
      <usgs>182.323516846</usgs>
    </waypoint>
    <waypoint id='799'>
      <lat>29.789807</lat>
      <lon>-98.0216</lon>
      <ele>180.9</ele>
      <usgs>182.796890259</usgs>
    </waypoint>
  </segment>

  <turn id='12'>
    <fromto>York Creek Rd. to Old Bastrop Rd.</fromto>
    <cue>RIGHT onto Old Bastrop Rd.</cue>
    <comments>York Creek Rd. dead-ends into Old Bastrop Rd.</comments>
  </turn>

  <segment id='13'>
    <road>Old Bastrop Rd.</road>
    <fromto>York Creek Rd. to FM 1102</fromto>
    <comments>You only stay on this road for little bit.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>35</speed>
    <waypoint id='800'>
      <lat>29.790066</lat>
      <lon>-98.021726</lon>
      <ele>180.9</ele>
      <usgs>182.548995972</usgs>
    </waypoint>
    <waypoint id='801'>
      <lat>29.790129</lat>
      <lon>-98.021731</lon>
      <ele>180.4</ele>
      <usgs>182.408782959</usgs>
    </waypoint>
    <waypoint id='802'>
      <lat>29.790537</lat>
      <lon>-98.021779</lon>
      <ele>180.4</ele>
      <usgs>182.218643188</usgs>
    </waypoint>
    <waypoint id='803'>
      <lat>29.790606</lat>
      <lon>-98.021795</lon>
      <ele>179.4</ele>
      <usgs>182.058609009</usgs>
    </waypoint>
    <waypoint id='804'>
      <lat>29.790891</lat>
      <lon>-98.021755</lon>
      <ele>178.5</ele>
      <usgs>181.839202881</usgs>
    </waypoint>
  </segment>

  <turn id='13'>
    <fromto>Old Bastrop Rd. to FM 1102</fromto>
    <cue>LEFT onto FM 1102 (no sign)</cue>
    <comments>Take you first left onto FM 1102.  
      There is no sign, but it's very obvious.</comments>
  </turn>

  <segment id='14'>
    <road>FM 1102</road>
    <fromto>Old Bastrop Rd. to Highway Overpass</fromto>
    <comments>Another short connector.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='805'>
      <lat>29.791186</lat>
      <lon>-98.021718</lon>
      <ele>179.4</ele>
      <usgs>182.206680298</usgs>
    </waypoint>
    <waypoint id='806'>
      <lat>29.791318</lat>
      <lon>-98.021862</lon>
      <ele>179.9</ele>
      <usgs>182.397003174</usgs>
    </waypoint>
    <waypoint id='807'>
      <lat>29.791723</lat>
      <lon>-98.022439</lon>
      <ele>179.4</ele>
      <usgs>182.648162842</usgs>
    </waypoint>
    <waypoint id='808'>
      <lat>29.791755</lat>
      <lon>-98.022481</lon>
      <ele>179.4</ele>
      <usgs>182.648162842</usgs>
    </waypoint>
  </segment>

  <turn id='14'>
    <fromto>FM 1102 to Highway Overpass</fromto>
    <cue>RIGHT onto Highway Overpass</cue>
    <comments>This one is very obvious.</comments>
  </turn>

  <segment id='15'>
    <road>Highway Overpass</road>
    <fromto>FM 1102 to FM 1102</fromto>
    <comments>Another highway department concoction.</comments>
    <lanes>2</lanes>
    <shoulder>1/2</shoulder>
    <traffic>Light</traffic>
    <speed>50</speed>
    <waypoint id='809'>
      <lat>29.792008</lat>
      <lon>-98.022639</lon>
      <ele>180.4</ele>
      <usgs>182.941864014</usgs>
    </waypoint>
    <waypoint id='810'>
      <lat>29.79224</lat>
      <lon>-98.022604</lon>
      <ele>181.3</ele>
      <usgs>184.046707153</usgs>
    </waypoint>
    <waypoint id='811'>
      <lat>29.792358</lat>
      <lon>-98.022524</lon>
      <ele>182.3</ele>
      <usgs>184.323257446</usgs>
    </waypoint>
    <waypoint id='812'>
      <lat>29.792704</lat>
      <lon>-98.022203</lon>
      <ele>184.2</ele>
      <usgs>185.35345459</usgs>
    </waypoint>
    <waypoint id='813'>
      <lat>29.792806</lat>
      <lon>-98.022119</lon>
      <ele>184.7</ele>
      <usgs>185.364212036</usgs>
    </waypoint>
    <waypoint id='814'>
      <lat>29.793059</lat>
      <lon>-98.022059</lon>
      <ele>186.6</ele>
      <usgs>186.859420776</usgs>
    </waypoint>
    <waypoint id='815'>
      <lat>29.793144</lat>
      <lon>-98.022083</lon>
      <ele>187.1</ele>
      <usgs>186.859420776</usgs>
    </waypoint>
    <waypoint id='816'>
      <lat>29.793379</lat>
      <lon>-98.022246</lon>
      <ele>188.1</ele>
      <usgs>189.274749756</usgs>
    </waypoint>
    <waypoint id='817'>
      <lat>29.793618</lat>
      <lon>-98.022455</lon>
      <ele>190.5</ele>
      <usgs>186.646865845</usgs>
    </waypoint>
    <waypoint id='818'>
      <lat>29.793906</lat>
      <lon>-98.022697</lon>
      <ele>191.0</ele>
      <usgs>186.630325317</usgs>
    </waypoint>
    <waypoint id='819'>
      <lat>29.794098</lat>
      <lon>-98.022851</lon>
      <ele>189.5</ele>
      <usgs>187.87348938</usgs>
    </waypoint>
    <waypoint id='820'>
      <lat>29.794392</lat>
      <lon>-98.023098</lon>
      <ele>188.1</ele>
      <usgs>189.220748901</usgs>
    </waypoint>
    <waypoint id='821'>
      <lat>29.794725</lat>
      <lon>-98.023438</lon>
      <ele>187.1</ele>
      <usgs>189.069015503</usgs>
    </waypoint>
    <waypoint id='822'>
      <lat>29.795106</lat>
      <lon>-98.023927</lon>
      <ele>184.7</ele>
      <usgs>185.103515625</usgs>
    </waypoint>
    <waypoint id='823'>
      <lat>29.795166</lat>
      <lon>-98.023989</lon>
      <ele>184.7</ele>
      <usgs>184.675140381</usgs>
    </waypoint>
    <waypoint id='824'>
      <lat>29.795512</lat>
      <lon>-98.024206</lon>
      <ele>184.2</ele>
      <usgs>183.938796997</usgs>
    </waypoint>
    <waypoint id='825'>
      <lat>29.795737</lat>
      <lon>-98.024255</lon>
      <ele>186.2</ele>
      <usgs>183.562438965</usgs>
    </waypoint>
  </segment>

  <turn id='15'>
    <fromto>Highway Overpass to FM 1102</fromto>
    <cue>RIGHT onto FM 1102</cue>
    <comments>Keep right after crossing the bridge and you'll end-up on FM
      1102.</comments>
  </turn>

  <segment id='16'>
    <road>FM 1102</road>
    <fromto>Highway Overpass to FM 1102</fromto>
    <comments>You'll go past fields, then you'll pass Riley's on the left after
      you cross the railroad tracks.</comments>
    <lanes>2</lanes>
    <shoulder>1/2</shoulder>
    <traffic>Light</traffic>
    <speed>50</speed>
    <waypoint id='826'>
      <lat>29.796217</lat>
      <lon>-98.024165</lon>
      <ele>185.7</ele>
      <usgs>183.218429565</usgs>
    </waypoint>
    <waypoint id='827'>
      <lat>29.796646</lat>
      <lon>-98.023941</lon>
      <ele>184.7</ele>
      <usgs>183.218017578</usgs>
    </waypoint>
    <waypoint id='828'>
      <lat>29.797049</lat>
      <lon>-98.023793</lon>
      <ele>184.2</ele>
      <usgs>183.278259277</usgs>
    </waypoint>
    <waypoint id='829'>
      <lat>29.79756</lat>
      <lon>-98.023722</lon>
      <ele>183.7</ele>
      <usgs>183.186203003</usgs>
    </waypoint>
    <waypoint id='830'>
      <lat>29.798051</lat>
      <lon>-98.023762</lon>
      <ele>184.7</ele>
      <usgs>183.315414429</usgs>
    </waypoint>
    <waypoint id='831'>
      <lat>29.7987</lat>
      <lon>-98.023903</lon>
      <ele>185.7</ele>
      <usgs>183.663574219</usgs>
    </waypoint>
    <waypoint id='832'>
      <lat>29.799556</lat>
      <lon>-98.024116</lon>
      <ele>186.2</ele>
      <usgs>185.266357422</usgs>
    </waypoint>
    <waypoint id='833'>
      <lat>29.800202</lat>
      <lon>-98.024283</lon>
      <ele>185.2</ele>
      <usgs>187.316741943</usgs>
    </waypoint>
    <waypoint id='834'>
      <lat>29.800949</lat>
      <lon>-98.024424</lon>
      <ele>186.6</ele>
      <usgs>188.070053101</usgs>
    </waypoint>
    <waypoint id='835'>
      <lat>29.801655</lat>
      <lon>-98.024439</lon>
      <ele>187.1</ele>
      <usgs>188.504928589</usgs>
    </waypoint>
    <waypoint id='836'>
      <lat>29.80255</lat>
      <lon>-98.024397</lon>
      <ele>187.6</ele>
      <usgs>188.780593872</usgs>
    </waypoint>
    <waypoint id='837'>
      <lat>29.802998</lat>
      <lon>-98.02429</lon>
      <ele>187.6</ele>
      <usgs>189.12677002</usgs>
    </waypoint>
    <waypoint id='838'>
      <lat>29.803272</lat>
      <lon>-98.024088</lon>
      <ele>188.1</ele>
      <usgs>189.395553589</usgs>
    </waypoint>
    <waypoint id='839'>
      <lat>29.803619</lat>
      <lon>-98.023658</lon>
      <ele>189.0</ele>
      <usgs>189.698104858</usgs>
    </waypoint>
    <waypoint id='840'>
      <lat>29.803974</lat>
      <lon>-98.023186</lon>
      <ele>188.6</ele>
      <usgs>189.937423706</usgs>
    </waypoint>
    <waypoint id='841'>
      <lat>29.804402</lat>
      <lon>-98.022636</lon>
      <ele>189.5</ele>
      <usgs>190.275527954</usgs>
    </waypoint>
    <waypoint id='842'>
      <lat>29.80468</lat>
      <lon>-98.022285</lon>
      <ele>191.0</ele>
      <usgs>190.413894653</usgs>
    </waypoint>
    <waypoint id='843'>
      <lat>29.804947</lat>
      <lon>-98.022147</lon>
      <ele>190.5</ele>
      <usgs>190.476013184</usgs>
    </waypoint>
    <waypoint id='844'>
      <lat>29.805174</lat>
      <lon>-98.022199</lon>
      <ele>191.0</ele>
      <usgs>190.529663086</usgs>
    </waypoint>
    <waypoint id='845'>
      <lat>29.805267</lat>
      <lon>-98.022266</lon>
      <ele>190.5</ele>
      <usgs>190.59197998</usgs>
    </waypoint>
    <waypoint id='846' stop='2'>
      <lat>29.805666</lat>
      <lon>-98.022674</lon>
      <ele>190.0</ele>
      <usgs>190.668716431</usgs>
    </waypoint>
    <waypoint id='847'>
      <lat>29.806016</lat>
      <lon>-98.023041</lon>
      <ele>190.0</ele>
      <usgs>190.431228638</usgs>
    </waypoint>
    <waypoint id='848'>
      <lat>29.8063</lat>
      <lon>-98.023316</lon>
      <ele>189.5</ele>
      <usgs>190.244628906</usgs>
    </waypoint>
    <waypoint id='849'>
      <lat>29.806587</lat>
      <lon>-98.023585</lon>
      <ele>191.4</ele>
      <usgs>189.979812622</usgs>
    </waypoint>
    <waypoint id='850'>
      <lat>29.806825</lat>
      <lon>-98.023799</lon>
      <ele>191.4</ele>
      <usgs>189.725234985</usgs>
    </waypoint>
  </segment>

  <turn id='16'>
    <fromto>FM 1102 to FM 1102</fromto>
    <cue>LEFT onto FM 1102</cue>
    <comments>FM 1102 dead-ends into FM 1102.</comments>
  </turn>

  <segment id='17'>
    <road>FM 1102</road>
    <fromto>FM 1102 to FM 1102</fromto>
    <comments>This road goes past some complex that is menacing and industrial,
      then passes country houses and fields. </comments>
    <lanes>2</lanes>
    <shoulder>2</shoulder>
    <traffic>Moderate</traffic>
    <speed>55</speed>
    <waypoint id='851'>
      <lat>29.807044</lat>
      <lon>-98.024004</lon>
      <ele>190.5</ele>
      <usgs>189.461502075</usgs>
    </waypoint>
    <waypoint id='852'>
      <lat>29.807037</lat>
      <lon>-98.024193</lon>
      <ele>191.0</ele>
      <usgs>188.735687256</usgs>
    </waypoint>
    <waypoint id='853'>
      <lat>29.80701</lat>
      <lon>-98.024239</lon>
      <ele>190.5</ele>
      <usgs>188.735687256</usgs>
    </waypoint>
    <waypoint id='854'>
      <lat>29.806739</lat>
      <lon>-98.024617</lon>
      <ele>189.5</ele>
      <usgs>187.975097656</usgs>
    </waypoint>
    <waypoint id='855'>
      <lat>29.806304</lat>
      <lon>-98.025218</lon>
      <ele>191.0</ele>
      <usgs>189.091064453</usgs>
    </waypoint>
    <waypoint id='856'>
      <lat>29.805973</lat>
      <lon>-98.025787</lon>
      <ele>191.0</ele>
      <usgs>189.722610474</usgs>
    </waypoint>
    <waypoint id='857'>
      <lat>29.80565</lat>
      <lon>-98.026543</lon>
      <ele>191.4</ele>
      <usgs>191.413650513</usgs>
    </waypoint>
    <waypoint id='858'>
      <lat>29.805333</lat>
      <lon>-98.027307</lon>
      <ele>191.9</ele>
      <usgs>193.727676392</usgs>
    </waypoint>
    <waypoint id='859'>
      <lat>29.804991</lat>
      <lon>-98.028133</lon>
      <ele>191.4</ele>
      <usgs>194.14175415</usgs>
    </waypoint>
    <waypoint id='860'>
      <lat>29.804646</lat>
      <lon>-98.028957</lon>
      <ele>192.9</ele>
      <usgs>193.92980957</usgs>
    </waypoint>
    <waypoint id='861'>
      <lat>29.804307</lat>
      <lon>-98.029774</lon>
      <ele>193.8</ele>
      <usgs>195.216827393</usgs>
    </waypoint>
    <waypoint id='862'>
      <lat>29.804019</lat>
      <lon>-98.030496</lon>
      <ele>194.8</ele>
      <usgs>195.753097534</usgs>
    </waypoint>
    <waypoint id='863'>
      <lat>29.803757</lat>
      <lon>-98.031287</lon>
      <ele>197.2</ele>
      <usgs>196.552566528</usgs>
    </waypoint>
    <waypoint id='864'>
      <lat>29.803637</lat>
      <lon>-98.031651</lon>
      <ele>198.6</ele>
      <usgs>197.745040894</usgs>
    </waypoint>
    <waypoint id='865'>
      <lat>29.803441</lat>
      <lon>-98.032178</lon>
      <ele>199.6</ele>
      <usgs>200.852325439</usgs>
    </waypoint>
    <waypoint id='866'>
      <lat>29.803142</lat>
      <lon>-98.032724</lon>
      <ele>200.1</ele>
      <usgs>201.58366394</usgs>
    </waypoint>
    <waypoint id='867'>
      <lat>29.802795</lat>
      <lon>-98.033171</lon>
      <ele>200.1</ele>
      <usgs>202.031723022</usgs>
    </waypoint>
    <waypoint id='868'>
      <lat>29.802283</lat>
      <lon>-98.033738</lon>
      <ele>201.5</ele>
      <usgs>201.837142944</usgs>
    </waypoint>
    <waypoint id='869'>
      <lat>29.801805</lat>
      <lon>-98.034252</lon>
      <ele>201.5</ele>
      <usgs>201.760955811</usgs>
    </waypoint>
    <waypoint id='870'>
      <lat>29.801255</lat>
      <lon>-98.034847</lon>
      <ele>202.0</ele>
      <usgs>201.478805542</usgs>
    </waypoint>
    <waypoint id='871'>
      <lat>29.800761</lat>
      <lon>-98.035394</lon>
      <ele>203.5</ele>
      <usgs>202.136123657</usgs>
    </waypoint>
    <waypoint id='872'>
      <lat>29.800517</lat>
      <lon>-98.035694</lon>
      <ele>203.5</ele>
      <usgs>202.783905029</usgs>
    </waypoint>
    <waypoint id='873'>
      <lat>29.8001</lat>
      <lon>-98.036232</lon>
      <ele>203.9</ele>
      <usgs>204.867767334</usgs>
    </waypoint>
    <waypoint id='874'>
      <lat>29.799765</lat>
      <lon>-98.03667</lon>
      <ele>206.3</ele>
      <usgs>206.036575317</usgs>
    </waypoint>
    <waypoint id='875'>
      <lat>29.799352</lat>
      <lon>-98.037194</lon>
      <ele>207.3</ele>
      <usgs>206.747253418</usgs>
    </waypoint>
    <waypoint id='876'>
      <lat>29.798877</lat>
      <lon>-98.037779</lon>
      <ele>206.8</ele>
      <usgs>208.36277771</usgs>
    </waypoint>
    <waypoint id='877'>
      <lat>29.798399</lat>
      <lon>-98.038316</lon>
      <ele>207.8</ele>
      <usgs>208.450820923</usgs>
    </waypoint>
    <waypoint id='878'>
      <lat>29.797862</lat>
      <lon>-98.038915</lon>
      <ele>207.8</ele>
      <usgs>208.115982056</usgs>
    </waypoint>
    <waypoint id='879'>
      <lat>29.797373</lat>
      <lon>-98.039467</lon>
      <ele>208.7</ele>
      <usgs>208.098083496</usgs>
    </waypoint>
    <waypoint id='880'>
      <lat>29.796888</lat>
      <lon>-98.040004</lon>
      <ele>207.3</ele>
      <usgs>209.052444458</usgs>
    </waypoint>
    <waypoint id='881'>
      <lat>29.796339</lat>
      <lon>-98.040614</lon>
      <ele>208.3</ele>
      <usgs>209.414398193</usgs>
    </waypoint>
    <waypoint id='882'>
      <lat>29.795708</lat>
      <lon>-98.041313</lon>
      <ele>208.3</ele>
      <usgs>210.287643433</usgs>
    </waypoint>
    <waypoint id='883'>
      <lat>29.795194</lat>
      <lon>-98.041881</lon>
      <ele>208.7</ele>
      <usgs>212.119338989</usgs>
    </waypoint>
    <waypoint id='884'>
      <lat>29.794688</lat>
      <lon>-98.04244</lon>
      <ele>210.2</ele>
      <usgs>214.220275879</usgs>
    </waypoint>
    <waypoint id='885'>
      <lat>29.794224</lat>
      <lon>-98.042959</lon>
      <ele>211.1</ele>
      <usgs>212.873855591</usgs>
    </waypoint>
    <waypoint id='886'>
      <lat>29.793636</lat>
      <lon>-98.043592</lon>
      <ele>214.0</ele>
      <usgs>216.092788696</usgs>
    </waypoint>
    <waypoint id='887'>
      <lat>29.79314</lat>
      <lon>-98.044046</lon>
      <ele>214.5</ele>
      <usgs>217.645675659</usgs>
    </waypoint>
    <waypoint id='888'>
      <lat>29.792535</lat>
      <lon>-98.044549</lon>
      <ele>216.0</ele>
      <usgs>218.989761353</usgs>
    </waypoint>
    <waypoint id='889'>
      <lat>29.792134</lat>
      <lon>-98.044925</lon>
      <ele>218.4</ele>
      <usgs>220.896774292</usgs>
    </waypoint>
    <waypoint id='890'>
      <lat>29.791769</lat>
      <lon>-98.045368</lon>
      <ele>217.4</ele>
      <usgs>220.983932495</usgs>
    </waypoint>
  </segment>

  <turn id='16a'>
    <fromto>FM 1102 to FM 1102</fromto>
    <cue>STRAIGHT on FM 1102</cue>
    <comments>This is where the shoulder narrows.</comments>
  </turn>

  <segment id='17a'>
    <road>FM 1102</road>
    <fromto>FM 1102 to Hunter Rd.</fromto>
    <comments>This part of FM 1102 has a narrow shoulder. </comments>
    <lanes>2</lanes>
    <shoulder>1/4</shoulder>
    <traffic>Moderate</traffic>
    <speed>55</speed>
    <waypoint id='891'>
      <lat>29.791285</lat>
      <lon>-98.045983</lon>
      <ele>217.9</ele>
      <usgs>220.378723145</usgs>
    </waypoint>
    <waypoint id='892'>
      <lat>29.790802</lat>
      <lon>-98.046643</lon>
      <ele>217.4</ele>
      <usgs>220.49281311</usgs>
    </waypoint>
    <waypoint id='893'>
      <lat>29.790422</lat>
      <lon>-98.047259</lon>
      <ele>217.4</ele>
      <usgs>220.232971191</usgs>
    </waypoint>
    <waypoint id='894'>
      <lat>29.790027</lat>
      <lon>-98.047919</lon>
      <ele>217.4</ele>
      <usgs>220.909194946</usgs>
    </waypoint>
    <waypoint id='895'>
      <lat>29.789654</lat>
      <lon>-98.048537</lon>
      <ele>216.9</ele>
      <usgs>221.600372314</usgs>
    </waypoint>
    <waypoint id='896'>
      <lat>29.789232</lat>
      <lon>-98.049228</lon>
      <ele>217.9</ele>
      <usgs>221.501739502</usgs>
    </waypoint>
    <waypoint id='897'>
      <lat>29.788768</lat>
      <lon>-98.049974</lon>
      <ele>220.8</ele>
      <usgs>224.679275513</usgs>
    </waypoint>
    <waypoint id='898'>
      <lat>29.788423</lat>
      <lon>-98.050507</lon>
      <ele>222.2</ele>
      <usgs>226.361831665</usgs>
    </waypoint>
    <waypoint id='899'>
      <lat>29.787998</lat>
      <lon>-98.051141</lon>
      <ele>222.2</ele>
      <usgs>227.756011963</usgs>
    </waypoint>
    <waypoint id='900'>
      <lat>29.787591</lat>
      <lon>-98.051708</lon>
      <ele>223.6</ele>
      <usgs>228.404388428</usgs>
    </waypoint>
    <waypoint id='901'>
      <lat>29.78718</lat>
      <lon>-98.052191</lon>
      <ele>224.1</ele>
      <usgs>227.877029419</usgs>
    </waypoint>
    <waypoint id='902'>
      <lat>29.786785</lat>
      <lon>-98.0526</lon>
      <ele>223.6</ele>
      <usgs>226.502822876</usgs>
    </waypoint>
    <waypoint id='903'>
      <lat>29.786539</lat>
      <lon>-98.05285</lon>
      <ele>222.7</ele>
      <usgs>225.434585571</usgs>
    </waypoint>
    <waypoint id='904'>
      <lat>29.786414</lat>
      <lon>-98.052976</lon>
      <ele>221.2</ele>
      <usgs>224.931152344</usgs>
    </waypoint>
    <waypoint id='905'>
      <lat>29.78589</lat>
      <lon>-98.053514</lon>
      <ele>222.2</ele>
      <usgs>227.0887146</usgs>
    </waypoint>
    <waypoint id='906'>
      <lat>29.785309</lat>
      <lon>-98.054116</lon>
      <ele>223.2</ele>
      <usgs>227.660568237</usgs>
    </waypoint>
    <waypoint id='907'>
      <lat>29.784718</lat>
      <lon>-98.054685</lon>
      <ele>224.6</ele>
      <usgs>227.094604492</usgs>
    </waypoint>
    <waypoint id='908'>
      <lat>29.78404</lat>
      <lon>-98.055197</lon>
      <ele>224.1</ele>
      <usgs>225.393066406</usgs>
    </waypoint>
    <waypoint id='909'>
      <lat>29.783375</lat>
      <lon>-98.055697</lon>
      <ele>222.2</ele>
      <usgs>223.968521118</usgs>
    </waypoint>
    <waypoint id='910'>
      <lat>29.782757</lat>
      <lon>-98.056151</lon>
      <ele>221.2</ele>
      <usgs>223.646743774</usgs>
    </waypoint>
    <waypoint id='911'>
      <lat>29.782096</lat>
      <lon>-98.056655</lon>
      <ele>221.7</ele>
      <usgs>224.001342773</usgs>
    </waypoint>
    <waypoint id='912'>
      <lat>29.781489</lat>
      <lon>-98.057244</lon>
      <ele>221.7</ele>
      <usgs>224.313034058</usgs>
    </waypoint>
    <waypoint id='913'>
      <lat>29.781075</lat>
      <lon>-98.057775</lon>
      <ele>221.2</ele>
      <usgs>223.250411987</usgs>
    </waypoint>
    <waypoint id='914'>
      <lat>29.780695</lat>
      <lon>-98.058432</lon>
      <ele>221.7</ele>
      <usgs>224.273040771</usgs>
    </waypoint>
    <waypoint id='915'>
      <lat>29.780256</lat>
      <lon>-98.059298</lon>
      <ele>221.7</ele>
      <usgs>225.473358154</usgs>
    </waypoint>
    <waypoint id='916'>
      <lat>29.779826</lat>
      <lon>-98.060148</lon>
      <ele>222.2</ele>
      <usgs>226.445373535</usgs>
    </waypoint>
    <waypoint id='917'>
      <lat>29.779384</lat>
      <lon>-98.061011</lon>
      <ele>223.6</ele>
      <usgs>224.748428345</usgs>
    </waypoint>
    <waypoint id='918'>
      <lat>29.778989</lat>
      <lon>-98.061618</lon>
      <ele>223.6</ele>
      <usgs>225.922409058</usgs>
    </waypoint>
    <waypoint id='919'>
      <lat>29.778565</lat>
      <lon>-98.062143</lon>
      <ele>224.1</ele>
      <usgs>228.706588745</usgs>
    </waypoint>
    <waypoint id='920'>
      <lat>29.778178</lat>
      <lon>-98.062581</lon>
      <ele>224.6</ele>
      <usgs>228.630432129</usgs>
    </waypoint>
    <waypoint id='921'>
      <lat>29.777711</lat>
      <lon>-98.063086</lon>
      <ele>223.6</ele>
      <usgs>228.893310547</usgs>
    </waypoint>
    <waypoint id='922'>
      <lat>29.777033</lat>
      <lon>-98.063767</lon>
      <ele>222.2</ele>
      <usgs>225.469360352</usgs>
    </waypoint>
    <waypoint id='923'>
      <lat>29.77697</lat>
      <lon>-98.063827</lon>
      <ele>222.2</ele>
      <usgs>225.275360107</usgs>
    </waypoint>
    <waypoint id='924'>
      <lat>29.776424</lat>
      <lon>-98.064335</lon>
      <ele>220.8</ele>
      <usgs>223.292800903</usgs>
    </waypoint>
    <waypoint id='925'>
      <lat>29.775791</lat>
      <lon>-98.064933</lon>
      <ele>217.9</ele>
      <usgs>219.528305054</usgs>
    </waypoint>
    <waypoint id='926'>
      <lat>29.77508</lat>
      <lon>-98.065561</lon>
      <ele>215.0</ele>
      <usgs>217.46232605</usgs>
    </waypoint>
    <waypoint id='927'>
      <lat>29.774922</lat>
      <lon>-98.065699</lon>
      <ele>214.5</ele>
      <usgs>217.29675293</usgs>
    </waypoint>
    <waypoint id='928'>
      <lat>29.774427</lat>
      <lon>-98.066198</lon>
      <ele>213.6</ele>
      <usgs>216.175308228</usgs>
    </waypoint>
    <waypoint id='929'>
      <lat>29.773838</lat>
      <lon>-98.066921</lon>
      <ele>214.5</ele>
      <usgs>218.264556885</usgs>
    </waypoint>
    <waypoint id='930'>
      <lat>29.77343</lat>
      <lon>-98.067433</lon>
      <ele>215.5</ele>
      <usgs>218.958908081</usgs>
    </waypoint>
    <waypoint id='931'>
      <lat>29.773342</lat>
      <lon>-98.067556</lon>
      <ele>216.4</ele>
      <usgs>218.911880493</usgs>
    </waypoint>
    <waypoint id='932'>
      <lat>29.773001</lat>
      <lon>-98.068115</lon>
      <ele>217.4</ele>
      <usgs>221.956863403</usgs>
    </waypoint>
    <waypoint id='933'>
      <lat>29.772732</lat>
      <lon>-98.06871</lon>
      <ele>218.8</ele>
      <usgs>223.893295288</usgs>
    </waypoint>
    <waypoint id='934'>
      <lat>29.772569</lat>
      <lon>-98.069104</lon>
      <ele>221.7</ele>
      <usgs>224.281051636</usgs>
    </waypoint>
    <waypoint id='935'>
      <lat>29.772384</lat>
      <lon>-98.069551</lon>
      <ele>221.7</ele>
      <usgs>224.265701294</usgs>
    </waypoint>
    <waypoint id='936'>
      <lat>29.772159</lat>
      <lon>-98.07007</lon>
      <ele>220.8</ele>
      <usgs>224.431671143</usgs>
    </waypoint>
    <waypoint id='937'>
      <lat>29.772033</lat>
      <lon>-98.070338</lon>
      <ele>221.2</ele>
      <usgs>224.662887573</usgs>
    </waypoint>
    <waypoint id='938'>
      <lat>29.771798</lat>
      <lon>-98.070808</lon>
      <ele>221.7</ele>
      <usgs>226.552871704</usgs>
    </waypoint>
    <waypoint id='939'>
      <lat>29.771411</lat>
      <lon>-98.071498</lon>
      <ele>222.2</ele>
      <usgs>227.442276001</usgs>
    </waypoint>
    <waypoint id='940'>
      <lat>29.77101</lat>
      <lon>-98.072093</lon>
      <ele>221.7</ele>
      <usgs>226.194030762</usgs>
    </waypoint>
    <waypoint id='941'>
      <lat>29.770613</lat>
      <lon>-98.072589</lon>
      <ele>221.7</ele>
      <usgs>225.628250122</usgs>
    </waypoint>
    <waypoint id='942'>
      <lat>29.77014</lat>
      <lon>-98.073128</lon>
      <ele>220.3</ele>
      <usgs>223.636444092</usgs>
    </waypoint>
    <waypoint id='943'>
      <lat>29.769624</lat>
      <lon>-98.073743</lon>
      <ele>218.8</ele>
      <usgs>221.446060181</usgs>
    </waypoint>
    <waypoint id='944'>
      <lat>29.769119</lat>
      <lon>-98.074321</lon>
      <ele>216.9</ele>
      <usgs>219.695419312</usgs>
    </waypoint>
    <waypoint id='945'>
      <lat>29.768447</lat>
      <lon>-98.075043</lon>
      <ele>214.5</ele>
      <usgs>215.02796936</usgs>
    </waypoint>
    <waypoint id='946'>
      <lat>29.767875</lat>
      <lon>-98.075496</lon>
      <ele>212.6</ele>
      <usgs>212.994552612</usgs>
    </waypoint>
    <waypoint id='947'>
      <lat>29.767364</lat>
      <lon>-98.075794</lon>
      <ele>213.1</ele>
      <usgs>212.471496582</usgs>
    </waypoint>
    <waypoint id='948'>
      <lat>29.767045</lat>
      <lon>-98.075915</lon>
      <ele>212.1</ele>
      <usgs>212.433959961</usgs>
    </waypoint>
  </segment>

  <turn id='17'>
    <fromto>FM 1102 to Hunter Rd.</fromto>
    <cue>RIGHT onto Hunter Rd.</cue>
    <comments>Hunter Rd. T's in on the right.  You went through here on the way
      out, so it may look familiar.</comments>
  </turn>

  <segment id='18'>
    <road>Hunter Rd.</road>
    <fromto>FM 1102 to Gruene Rd.</fromto>
    <comments>You came out on Hunter Rd., so your feeling of deja-vu is
      justified.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='949'>
      <lat>29.766805</lat>
      <lon>-98.076106</lon>
      <ele>210.7</ele>
      <usgs>212.379394531</usgs>
    </waypoint>
    <waypoint id='950'>
      <lat>29.766783</lat>
      <lon>-98.076187</lon>
      <ele>210.2</ele>
      <usgs>212.328826904</usgs>
    </waypoint>
    <waypoint id='951'>
      <lat>29.766783</lat>
      <lon>-98.076452</lon>
      <ele>210.7</ele>
      <usgs>212.189956665</usgs>
    </waypoint>
    <waypoint id='952'>
      <lat>29.766722</lat>
      <lon>-98.076709</lon>
      <ele>211.6</ele>
      <usgs>212.007171631</usgs>
    </waypoint>
    <waypoint id='953'>
      <lat>29.766624</lat>
      <lon>-98.076848</lon>
      <ele>212.1</ele>
      <usgs>212.025634766</usgs>
    </waypoint>
    <waypoint id='954'>
      <lat>29.766129</lat>
      <lon>-98.077375</lon>
      <ele>213.1</ele>
      <usgs>213.162368774</usgs>
    </waypoint>
    <waypoint id='955'>
      <lat>29.765793</lat>
      <lon>-98.077713</lon>
      <ele>212.6</ele>
      <usgs>213.954666138</usgs>
    </waypoint>
    <waypoint id='956'>
      <lat>29.765412</lat>
      <lon>-98.078103</lon>
      <ele>213.1</ele>
      <usgs>215.074188232</usgs>
    </waypoint>
    <waypoint id='957'>
      <lat>29.765298</lat>
      <lon>-98.078228</lon>
      <ele>211.1</ele>
      <usgs>215.571838379</usgs>
    </waypoint>
    <waypoint id='958'>
      <lat>29.765161</lat>
      <lon>-98.078376</lon>
      <ele>215.0</ele>
      <usgs>216.844329834</usgs>
    </waypoint>
    <waypoint id='959'>
      <lat>29.765062</lat>
      <lon>-98.078491</lon>
      <ele>214.0</ele>
      <usgs>217.396820068</usgs>
    </waypoint>
    <waypoint id='960'>
      <lat>29.764742</lat>
      <lon>-98.078831</lon>
      <ele>216.9</ele>
      <usgs>218.613861084</usgs>
    </waypoint>
    <waypoint id='961'>
      <lat>29.764453</lat>
      <lon>-98.07913</lon>
      <ele>216.9</ele>
      <usgs>219.906707764</usgs>
    </waypoint>
    <waypoint id='962'>
      <lat>29.764088</lat>
      <lon>-98.079524</lon>
      <ele>218.8</ele>
      <usgs>221.419937134</usgs>
    </waypoint>
    <waypoint id='963'>
      <lat>29.763823</lat>
      <lon>-98.079816</lon>
      <ele>220.8</ele>
      <usgs>222.857131958</usgs>
    </waypoint>
    <waypoint id='964'>
      <lat>29.763562</lat>
      <lon>-98.080112</lon>
      <ele>221.2</ele>
      <usgs>224.170318604</usgs>
    </waypoint>
    <waypoint id='965'>
      <lat>29.763426</lat>
      <lon>-98.080269</lon>
      <ele>225.6</ele>
      <usgs>224.599502563</usgs>
    </waypoint>
    <waypoint id='966'>
      <lat>29.763392</lat>
      <lon>-98.080312</lon>
      <ele>220.3</ele>
      <usgs>225.136184692</usgs>
    </waypoint>
    <waypoint id='967'>
      <lat>29.763211</lat>
      <lon>-98.080525</lon>
      <ele>220.8</ele>
      <usgs>225.797164917</usgs>
    </waypoint>
    <waypoint id='968'>
      <lat>29.76298</lat>
      <lon>-98.080774</lon>
      <ele>222.2</ele>
      <usgs>224.92477417</usgs>
    </waypoint>
    <waypoint id='969'>
      <lat>29.762603</lat>
      <lon>-98.081197</lon>
      <ele>220.8</ele>
      <usgs>223.851394653</usgs>
    </waypoint>
    <waypoint id='970'>
      <lat>29.762008</lat>
      <lon>-98.081856</lon>
      <ele>221.2</ele>
      <usgs>223.229324341</usgs>
    </waypoint>
    <waypoint id='971'>
      <lat>29.761679</lat>
      <lon>-98.082241</lon>
      <ele>222.2</ele>
      <usgs>224.011978149</usgs>
    </waypoint>
    <waypoint id='972'>
      <lat>29.761454</lat>
      <lon>-98.082622</lon>
      <ele>222.2</ele>
      <usgs>224.953842163</usgs>
    </waypoint>
    <waypoint id='973'>
      <lat>29.761329</lat>
      <lon>-98.083057</lon>
      <ele>224.1</ele>
      <usgs>225.570571899</usgs>
    </waypoint>
    <waypoint id='974'>
      <lat>29.761271</lat>
      <lon>-98.083297</lon>
      <ele>225.1</ele>
      <usgs>225.363464355</usgs>
    </waypoint>
    <waypoint id='975'>
      <lat>29.761137</lat>
      <lon>-98.083884</lon>
      <ele>225.1</ele>
      <usgs>226.004425049</usgs>
    </waypoint>
    <waypoint id='976'>
      <lat>29.760977</lat>
      <lon>-98.084564</lon>
      <ele>225.6</ele>
      <usgs>226.319595337</usgs>
    </waypoint>
    <waypoint id='977'>
      <lat>29.760775</lat>
      <lon>-98.085469</lon>
      <ele>222.2</ele>
      <usgs>224.720718384</usgs>
    </waypoint>
    <waypoint id='978'>
      <lat>29.760676</lat>
      <lon>-98.085915</lon>
      <ele>221.7</ele>
      <usgs>224.375015259</usgs>
    </waypoint>
    <waypoint id='979'>
      <lat>29.760569</lat>
      <lon>-98.086274</lon>
      <ele>221.2</ele>
      <usgs>224.112854004</usgs>
    </waypoint>
    <waypoint id='980'>
      <lat>29.760404</lat>
      <lon>-98.086514</lon>
      <ele>221.7</ele>
      <usgs>224.124328613</usgs>
    </waypoint>
    <waypoint id='981'>
      <lat>29.759866</lat>
      <lon>-98.086962</lon>
      <ele>221.2</ele>
      <usgs>224.060089111</usgs>
    </waypoint>
    <waypoint id='982'>
      <lat>29.759267</lat>
      <lon>-98.087429</lon>
      <ele>221.2</ele>
      <usgs>224.467956543</usgs>
    </waypoint>
    <waypoint id='983'>
      <lat>29.758681</lat>
      <lon>-98.08789</lon>
      <ele>220.8</ele>
      <usgs>222.341781616</usgs>
    </waypoint>
    <waypoint id='984'>
      <lat>29.758122</lat>
      <lon>-98.088341</lon>
      <ele>219.3</ele>
      <usgs>220.695098877</usgs>
    </waypoint>
    <waypoint id='985'>
      <lat>29.757509</lat>
      <lon>-98.088842</lon>
      <ele>217.9</ele>
      <usgs>219.858428955</usgs>
    </waypoint>
    <waypoint id='986'>
      <lat>29.756892</lat>
      <lon>-98.089314</lon>
      <ele>216.0</ele>
      <usgs>218.095077515</usgs>
    </waypoint>
    <waypoint id='987'>
      <lat>29.756214</lat>
      <lon>-98.089836</lon>
      <ele>216.0</ele>
      <usgs>215.342819214</usgs>
    </waypoint>
    <waypoint id='988'>
      <lat>29.755586</lat>
      <lon>-98.090417</lon>
      <ele>214.0</ele>
      <usgs>214.487594604</usgs>
    </waypoint>
    <waypoint id='989'>
      <lat>29.754864</lat>
      <lon>-98.09114</lon>
      <ele>212.1</ele>
      <usgs>213.716796875</usgs>
    </waypoint>
    <waypoint id='990'>
      <lat>29.754273</lat>
      <lon>-98.091653</lon>
      <ele>211.1</ele>
      <usgs>213.011566162</usgs>
    </waypoint>
    <waypoint id='991'>
      <lat>29.753674</lat>
      <lon>-98.092114</lon>
      <ele>210.7</ele>
      <usgs>212.414230347</usgs>
    </waypoint>
    <waypoint id='992'>
      <lat>29.753375</lat>
      <lon>-98.092341</lon>
      <ele>211.1</ele>
      <usgs>212.288406372</usgs>
    </waypoint>
    <waypoint id='993'>
      <lat>29.753072</lat>
      <lon>-98.092563</lon>
      <ele>208.7</ele>
      <usgs>211.481658936</usgs>
    </waypoint>
    <waypoint id='994'>
      <lat>29.752686</lat>
      <lon>-98.092824</lon>
      <ele>207.8</ele>
      <usgs>209.906066895</usgs>
    </waypoint>
    <waypoint id='995'>
      <lat>29.752498</lat>
      <lon>-98.092932</lon>
      <ele>207.3</ele>
      <usgs>209.3409729</usgs>
    </waypoint>
    <waypoint id='996'>
      <lat>29.752292</lat>
      <lon>-98.093036</lon>
      <ele>206.3</ele>
      <usgs>209.04624939</usgs>
    </waypoint>
    <waypoint id='997'>
      <lat>29.752163</lat>
      <lon>-98.093088</lon>
      <ele>206.8</ele>
      <usgs>208.779251099</usgs>
    </waypoint>
    <waypoint id='998'>
      <lat>29.75212</lat>
      <lon>-98.093095</lon>
      <ele>205.9</ele>
      <usgs>208.824356079</usgs>
    </waypoint>
    <waypoint id='999'>
      <lat>29.752123</lat>
      <lon>-98.093091</lon>
      <ele>207.3</ele>
      <usgs>208.824356079</usgs>
    </waypoint>
    <waypoint id='1000'>
      <lat>29.752027</lat>
      <lon>-98.093104</lon>
      <ele>207.3</ele>
      <usgs>208.871307373</usgs>
    </waypoint>
    <waypoint id='1001'>
      <lat>29.751864</lat>
      <lon>-98.093027</lon>
      <ele>208.3</ele>
      <usgs>209.124389648</usgs>
    </waypoint>
    <waypoint id='1002'>
      <lat>29.75165</lat>
      <lon>-98.092792</lon>
      <ele>208.7</ele>
      <usgs>209.557418823</usgs>
    </waypoint>
    <waypoint id='1003'>
      <lat>29.751287</lat>
      <lon>-98.092364</lon>
      <ele>209.7</ele>
      <usgs>210.369842529</usgs>
    </waypoint>
    <waypoint id='1004'>
      <lat>29.75094</lat>
      <lon>-98.091953</lon>
      <ele>210.2</ele>
      <usgs>210.819946289</usgs>
    </waypoint>
    <waypoint id='1005'>
      <lat>29.750499</lat>
      <lon>-98.091424</lon>
      <ele>210.2</ele>
      <usgs>211.358001709</usgs>
    </waypoint>
    <waypoint id='1006'>
      <lat>29.750184</lat>
      <lon>-98.091053</lon>
      <ele>210.7</ele>
      <usgs>211.66355896</usgs>
    </waypoint>
    <waypoint id='1007'>
      <lat>29.749924</lat>
      <lon>-98.090935</lon>
      <ele>210.2</ele>
      <usgs>211.807403564</usgs>
    </waypoint>
    <waypoint id='1008'>
      <lat>29.749763</lat>
      <lon>-98.090998</lon>
      <ele>210.2</ele>
      <usgs>211.892868042</usgs>
    </waypoint>
    <waypoint id='1009'>
      <lat>29.749675</lat>
      <lon>-98.091076</lon>
      <ele>210.7</ele>
      <usgs>211.873168945</usgs>
    </waypoint>
    <waypoint id='1010'>
      <lat>29.749143</lat>
      <lon>-98.091682</lon>
      <ele>209.7</ele>
      <usgs>211.661636353</usgs>
    </waypoint>
    <waypoint id='1011'>
      <lat>29.748791</lat>
      <lon>-98.092097</lon>
      <ele>211.1</ele>
      <usgs>211.503372192</usgs>
    </waypoint>
    <waypoint id='1012'>
      <lat>29.748288</lat>
      <lon>-98.09267</lon>
      <ele>210.2</ele>
      <usgs>211.287033081</usgs>
    </waypoint>
    <waypoint id='1013'>
      <lat>29.747768</lat>
      <lon>-98.093267</lon>
      <ele>209.7</ele>
      <usgs>210.904464722</usgs>
    </waypoint>
    <waypoint id='1014'>
      <lat>29.747136</lat>
      <lon>-98.093995</lon>
      <ele>209.2</ele>
      <usgs>210.363037109</usgs>
    </waypoint>
    <waypoint id='1015'>
      <lat>29.746573</lat>
      <lon>-98.094645</lon>
      <ele>208.7</ele>
      <usgs>208.934326172</usgs>
    </waypoint>
    <waypoint id='1016'>
      <lat>29.746372</lat>
      <lon>-98.094878</lon>
      <ele>206.8</ele>
      <usgs>208.454605103</usgs>
    </waypoint>
    <waypoint id='1017'>
      <lat>29.745717</lat>
      <lon>-98.095636</lon>
      <ele>206.3</ele>
      <usgs>207.12461853</usgs>
    </waypoint>
    <waypoint id='1018'>
      <lat>29.745079</lat>
      <lon>-98.096368</lon>
      <ele>206.3</ele>
      <usgs>206.835739136</usgs>
    </waypoint>
    <waypoint id='1019'>
      <lat>29.744686</lat>
      <lon>-98.096883</lon>
      <ele>206.3</ele>
      <usgs>206.961914062</usgs>
    </waypoint>
    <waypoint id='1020'>
      <lat>29.744408</lat>
      <lon>-98.097333</lon>
      <ele>205.4</ele>
      <usgs>206.944213867</usgs>
    </waypoint>
    <waypoint id='1021'>
      <lat>29.74426</lat>
      <lon>-98.097583</lon>
      <ele>204.9</ele>
      <usgs>206.811050415</usgs>
    </waypoint>
    <waypoint id='1022'>
      <lat>29.744206</lat>
      <lon>-98.097684</lon>
      <ele>203.5</ele>
      <usgs>206.850341797</usgs>
    </waypoint>
    <waypoint id='1023' stop='0'>
      <lat>29.744133</lat>
      <lon>-98.097805</lon>
      <ele>205.4</ele>
      <usgs>206.636810303</usgs>
    </waypoint>
    <waypoint id='1024'>
      <lat>29.743914</lat>
      <lon>-98.098168</lon>
      <ele>205.9</ele>
      <usgs>206.114746094</usgs>
    </waypoint>
    <waypoint id='1025'>
      <lat>29.743619</lat>
      <lon>-98.098674</lon>
      <ele>205.4</ele>
      <usgs>205.406143188</usgs>
    </waypoint>
    <waypoint id='1026'>
      <lat>29.743268</lat>
      <lon>-98.099245</lon>
      <ele>204.9</ele>
      <usgs>205.232910156</usgs>
    </waypoint>
    <waypoint id='1027'>
      <lat>29.743127</lat>
      <lon>-98.099474</lon>
      <ele>206.3</ele>
      <usgs>205.361999512</usgs>
    </waypoint>
    <waypoint id='1028'>
      <lat>29.742847</lat>
      <lon>-98.099951</lon>
      <ele>203.9</ele>
      <usgs>205.434906006</usgs>
    </waypoint>
    <waypoint id='1029'>
      <lat>29.742438</lat>
      <lon>-98.100617</lon>
      <ele>202.5</ele>
      <usgs>204.62322998</usgs>
    </waypoint>
    <waypoint id='1030'>
      <lat>29.742072</lat>
      <lon>-98.101144</lon>
      <ele>203.0</ele>
      <usgs>203.468795776</usgs>
    </waypoint>
    <waypoint id='1031'>
      <lat>29.741796</lat>
      <lon>-98.101436</lon>
      <ele>203.0</ele>
      <usgs>203.140014648</usgs>
    </waypoint>
    <waypoint id='1032'>
      <lat>29.741378</lat>
      <lon>-98.101731</lon>
      <ele>202.0</ele>
      <usgs>202.579406738</usgs>
    </waypoint>
    <waypoint id='1033'>
      <lat>29.740906</lat>
      <lon>-98.102036</lon>
      <ele>203.0</ele>
      <usgs>202.633422852</usgs>
    </waypoint>
    <waypoint id='1034'>
      <lat>29.740368</lat>
      <lon>-98.102359</lon>
      <ele>204.4</ele>
      <usgs>204.856552124</usgs>
    </waypoint>
    <waypoint id='1035'>
      <lat>29.740316</lat>
      <lon>-98.102388</lon>
      <ele>203.9</ele>
      <usgs>204.856552124</usgs>
    </waypoint>
    <waypoint id='1036'>
      <lat>29.739809</lat>
      <lon>-98.102715</lon>
      <ele>205.9</ele>
      <usgs>207.428100586</usgs>
    </waypoint>
    <waypoint id='1037'>
      <lat>29.739286</lat>
      <lon>-98.103159</lon>
      <ele>206.3</ele>
      <usgs>206.893493652</usgs>
    </waypoint>
    <waypoint id='1038'>
      <lat>29.739129</lat>
      <lon>-98.103278</lon>
      <ele>205.4</ele>
      <usgs>206.851913452</usgs>
    </waypoint>
    <waypoint id='1109'>
      <lat>29.739047</lat>
      <lon>-98.103413</lon>
      <ele>203.5</ele>
      <usgs>206.881622314</usgs>
    </waypoint>
    <waypoint id='1110'>
      <lat>29.738891</lat>
      <lon>-98.103607</lon>
      <ele>202.5</ele>
      <usgs>206.787734985</usgs>
    </waypoint>
    <waypoint id='1111'>
      <lat>29.738745</lat>
      <lon>-98.103813</lon>
      <ele>202.5</ele>
      <usgs>206.310760498</usgs>
    </waypoint>
    <waypoint id='1112'>
      <lat>29.73861</lat>
      <lon>-98.104021</lon>
      <ele>202.5</ele>
      <usgs>205.987976074</usgs>
    </waypoint>
    <waypoint id='1113'>
      <lat>29.738539</lat>
      <lon>-98.104149</lon>
      <ele>201.5</ele>
      <usgs>205.798934937</usgs>
    </waypoint>
  </segment>

  <turn id='18'>
    <fromto>Hunter Rd. to Gruene Rd.</fromto>
    <cue>LEFT onto Gruene Rd.</cue>
    <comments>Hunter Rd. dead-ends into Gruene Rd. in Gruene right in front of
      Gruene Hall.</comments>
  </turn>

  <segment id='19'>
    <road>Gruene Rd.</road>
    <fromto>Hunter Rd. to parking</fromto>
    <comments>You're done!</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>40</speed>
    <waypoint id='1114'>
      <lat>29.738478</lat>
      <lon>-98.104202</lon>
      <ele>202.0</ele>
      <usgs>205.738479614</usgs>
    </waypoint>
    <waypoint id='1115'>
      <lat>29.738324</lat>
      <lon>-98.104131</lon>
      <ele>203.0</ele>
      <usgs>205.982925415</usgs>
    </waypoint>
    <waypoint id='1116'>
      <lat>29.738291</lat>
      <lon>-98.104103</lon>
      <ele>203.0</ele>
      <usgs>205.982925415</usgs>
    </waypoint>
  </segment>

  <turn id='26'>
    <fromto>parking to Gruene Rd.</fromto>
    <cue>RIGHT onto Gruene Rd.</cue>
    <comments>This is in a northwest direction, towards the big
    downhill.</comments>
  </turn>

  <segment id='26'>
    <road>Gruene Rd.</road>
    <fromto>parking to Gruene Rd.</fromto>
    <comments>You'll go almost immediately down the steep hill and over the
      river, then through woods and neighborhoods.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='1511' stop='0a'>
      <lat>29.738195</lat>
      <lon>-98.104082</lon>
      <ele>207.8</ele>
      <usgs>205.993453979</usgs>
    </waypoint>
    <waypoint id='1512'>
      <lat>29.738216</lat>
      <lon>-98.104107</lon>
      <ele>207.8</ele>
      <usgs>205.993453979</usgs>
    </waypoint>
    <waypoint id='1513'>
      <lat>29.738495</lat>
      <lon>-98.104334</lon>
      <ele>207.3</ele>
      <usgs>205.609481812</usgs>
    </waypoint>
    <waypoint id='1514'>
      <lat>29.73873</lat>
      <lon>-98.104517</lon>
      <ele>206.8</ele>
      <usgs>205.088104248</usgs>
    </waypoint>
    <waypoint id='1515'>
      <lat>29.739012</lat>
      <lon>-98.104763</lon>
      <ele>204.9</ele>
      <usgs>204.086273193</usgs>
    </waypoint>
    <waypoint id='1516'>
      <lat>29.739077</lat>
      <lon>-98.104967</lon>
      <ele>203.9</ele>
      <usgs>202.199508667</usgs>
    </waypoint>
    <waypoint id='1517'>
      <lat>29.739031</lat>
      <lon>-98.105179</lon>
      <ele>203.0</ele>
      <usgs>200.430969238</usgs>
    </waypoint>
    <waypoint id='1518'>
      <lat>29.738867</lat>
      <lon>-98.10565</lon>
      <ele>201.1</ele>
      <usgs>193.39831543</usgs>
    </waypoint>
    <waypoint id='1519'>
      <lat>29.738572</lat>
      <lon>-98.106043</lon>
      <ele>195.3</ele>
      <usgs>185.78338623</usgs>
    </waypoint>
    <waypoint id='1520'>
      <lat>29.738467</lat>
      <lon>-98.106114</lon>
      <ele>193.4</ele>
      <usgs>184.318557739</usgs>
    </waypoint>
    <waypoint id='1521'>
      <lat>29.737945</lat>
      <lon>-98.106398</lon>
      <ele>191.9</ele>
      <usgs>184.556640625</usgs>
    </waypoint>
    <waypoint id='1522'>
      <lat>29.737672</lat>
      <lon>-98.106713</lon>
      <ele>191.9</ele>
      <usgs>185.442016602</usgs>
    </waypoint>
    <waypoint id='1523'>
      <lat>29.737619</lat>
      <lon>-98.106793</lon>
      <ele>191.9</ele>
      <usgs>185.59161377</usgs>
    </waypoint>
    <waypoint id='1524'>
      <lat>29.737396</lat>
      <lon>-98.107129</lon>
      <ele>191.9</ele>
      <usgs>186.382339478</usgs>
    </waypoint>
    <waypoint id='1525'>
      <lat>29.737189</lat>
      <lon>-98.107439</lon>
      <ele>191.4</ele>
      <usgs>187.652130127</usgs>
    </waypoint>
    <waypoint id='1526'>
      <lat>29.736955</lat>
      <lon>-98.107792</lon>
      <ele>191.9</ele>
      <usgs>188.556686401</usgs>
    </waypoint>
    <waypoint id='1527'>
      <lat>29.736712</lat>
      <lon>-98.108177</lon>
      <ele>192.9</ele>
      <usgs>189.701889038</usgs>
    </waypoint>
    <waypoint id='1528'>
      <lat>29.736527</lat>
      <lon>-98.108469</lon>
      <ele>194.3</ele>
      <usgs>190.805282593</usgs>
    </waypoint>
    <waypoint id='1529'>
      <lat>29.736286</lat>
      <lon>-98.108854</lon>
      <ele>194.8</ele>
      <usgs>192.42515564</usgs>
    </waypoint>
    <waypoint id='1530'>
      <lat>29.736008</lat>
      <lon>-98.109294</lon>
      <ele>196.2</ele>
      <usgs>193.33001709</usgs>
    </waypoint>
    <waypoint id='1531'>
      <lat>29.735682</lat>
      <lon>-98.109797</lon>
      <ele>198.2</ele>
      <usgs>195.451477051</usgs>
    </waypoint>
    <waypoint id='1532'>
      <lat>29.735322</lat>
      <lon>-98.11034</lon>
      <ele>198.2</ele>
      <usgs>195.502563477</usgs>
    </waypoint>
    <waypoint id='1533'>
      <lat>29.73505</lat>
      <lon>-98.110744</lon>
      <ele>199.1</ele>
      <usgs>195.683547974</usgs>
    </waypoint>
    <waypoint id='1534'>
      <lat>29.734786</lat>
      <lon>-98.111176</lon>
      <ele>199.1</ele>
      <usgs>196.225784302</usgs>
    </waypoint>
    <waypoint id='1535'>
      <lat>29.734538</lat>
      <lon>-98.111591</lon>
      <ele>199.1</ele>
      <usgs>197.443710327</usgs>
    </waypoint>
    <waypoint id='1536'>
      <lat>29.734352</lat>
      <lon>-98.111938</lon>
      <ele>201.1</ele>
      <usgs>197.754684448</usgs>
    </waypoint>
    <waypoint id='1537'>
      <lat>29.734099</lat>
      <lon>-98.112422</lon>
      <ele>203.5</ele>
      <usgs>201.722335815</usgs>
    </waypoint>
    <waypoint id='1538'>
      <lat>29.733912</lat>
      <lon>-98.112938</lon>
      <ele>204.4</ele>
      <usgs>201.81980896</usgs>
    </waypoint>
    <waypoint id='1539'>
      <lat>29.733697</lat>
      <lon>-98.113424</lon>
      <ele>203.9</ele>
      <usgs>201.705429077</usgs>
    </waypoint>
    <waypoint id='1540'>
      <lat>29.733486</lat>
      <lon>-98.11375</lon>
      <ele>204.4</ele>
      <usgs>201.761520386</usgs>
    </waypoint>
    <waypoint id='1541'>
      <lat>29.733106</lat>
      <lon>-98.114275</lon>
      <ele>205.4</ele>
      <usgs>201.809341431</usgs>
    </waypoint>
    <waypoint id='1542'>
      <lat>29.732613</lat>
      <lon>-98.114893</lon>
      <ele>205.9</ele>
      <usgs>201.733215332</usgs>
    </waypoint>
    <waypoint id='1543'>
      <lat>29.732169</lat>
      <lon>-98.115428</lon>
      <ele>205.4</ele>
      <usgs>201.923919678</usgs>
    </waypoint>
    <waypoint id='1544'>
      <lat>29.731896</lat>
      <lon>-98.115631</lon>
      <ele>205.4</ele>
      <usgs>201.897079468</usgs>
    </waypoint>
    <waypoint id='1545'>
      <lat>29.731415</lat>
      <lon>-98.11588</lon>
      <ele>204.4</ele>
      <usgs>200.901672363</usgs>
    </waypoint>
    <waypoint id='1546'>
      <lat>29.73066</lat>
      <lon>-98.116254</lon>
      <ele>203.5</ele>
      <usgs>200.475463867</usgs>
    </waypoint>
    <waypoint id='1547'>
      <lat>29.730131</lat>
      <lon>-98.116569</lon>
      <ele>202.0</ele>
      <usgs>197.47442627</usgs>
    </waypoint>
    <waypoint id='1548'>
      <lat>29.729541</lat>
      <lon>-98.116918</lon>
      <ele>199.6</ele>
      <usgs>197.607223511</usgs>
    </waypoint>
    <waypoint id='1549'>
      <lat>29.728907</lat>
      <lon>-98.117295</lon>
      <ele>201.1</ele>
      <usgs>197.685348511</usgs>
    </waypoint>
    <waypoint id='1550'>
      <lat>29.728054</lat>
      <lon>-98.117798</lon>
      <ele>201.5</ele>
      <usgs>197.58555603</usgs>
    </waypoint>
    <waypoint id='1551'>
      <lat>29.727234</lat>
      <lon>-98.118289</lon>
      <ele>201.1</ele>
      <usgs>197.820846558</usgs>
    </waypoint>
    <waypoint id='1552'>
      <lat>29.726636</lat>
      <lon>-98.118653</lon>
      <ele>201.1</ele>
      <usgs>198.150238037</usgs>
    </waypoint>
    <waypoint id='1553'>
      <lat>29.725753</lat>
      <lon>-98.119186</lon>
      <ele>199.6</ele>
      <usgs>197.968658447</usgs>
    </waypoint>
    <waypoint id='1554'>
      <lat>29.725696</lat>
      <lon>-98.119216</lon>
      <ele>199.6</ele>
      <usgs>197.579330444</usgs>
    </waypoint>
    <waypoint id='1555'>
      <lat>29.725453</lat>
      <lon>-98.119233</lon>
      <ele>199.1</ele>
      <usgs>196.213348389</usgs>
    </waypoint>
    <waypoint id='1556'>
      <lat>29.725295</lat>
      <lon>-98.11911</lon>
      <ele>198.2</ele>
      <usgs>196.047363281</usgs>
    </waypoint>
    <waypoint id='1557'>
      <lat>29.724869</lat>
      <lon>-98.118637</lon>
      <ele>195.8</ele>
      <usgs>193.688720703</usgs>
    </waypoint>
    <waypoint id='1558'>
      <lat>29.724334</lat>
      <lon>-98.118041</lon>
      <ele>194.8</ele>
      <usgs>191.498794556</usgs>
    </waypoint>
    <waypoint id='1559'>
      <lat>29.723949</lat>
      <lon>-98.117622</lon>
      <ele>192.9</ele>
      <usgs>190.708312988</usgs>
    </waypoint>
  </segment>

  <turn id='27'>
    <fromto>Gruene Rd. to Torrey St.</fromto>
    <cue>RIGHT onto Torrey St.</cue>
    <comments></comments>
  </turn>

  <segment id='27'>
    <road>Torrey St.</road>
    <fromto>Gruene Rd. to Lakeview Blvd.</fromto>
    <comments>Residential street</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='12582'>
      <lat>29.723772</lat>
      <lon>-98.117469</lon>
      <ele>188.6</ele>
      <usgs>190.145874023</usgs>
    </waypoint>
    <waypoint id='12581'>
      <lat>29.723739</lat>
      <lon>-98.117494</lon>
      <ele>188.1</ele>
      <usgs>190.145874023</usgs>
    </waypoint>
    <waypoint id='12580'>
      <lat>29.723545</lat>
      <lon>-98.117698</lon>
      <ele>188.6</ele>
      <usgs>189.889312744</usgs>
    </waypoint>
    <waypoint id='12579'>
      <lat>29.723095</lat>
      <lon>-98.118184</lon>
      <ele>189.0</ele>
      <usgs>190.061660767</usgs>
    </waypoint>
    <waypoint id='12578'>
      <lat>29.722609</lat>
      <lon>-98.118706</lon>
      <ele>189.5</ele>
      <usgs>190.650939941</usgs>
    </waypoint>
    <waypoint id='12577'>
      <lat>29.722167</lat>
      <lon>-98.119184</lon>
      <ele>189.5</ele>
      <usgs>193.339141846</usgs>
    </waypoint>
    <waypoint id='12576'>
      <lat>29.721704</lat>
      <lon>-98.119686</lon>
      <ele>189.5</ele>
      <usgs>194.352416992</usgs>
    </waypoint>
    <waypoint id='12575'>
      <lat>29.721298</lat>
      <lon>-98.12013</lon>
      <ele>190.0</ele>
      <usgs>193.051300049</usgs>
    </waypoint>
    <waypoint id='12574'>
      <lat>29.720862</lat>
      <lon>-98.120581</lon>
      <ele>190.0</ele>
      <usgs>192.236572266</usgs>
    </waypoint>
    <waypoint id='12573'>
      <lat>29.720462</lat>
      <lon>-98.121008</lon>
      <ele>191.0</ele>
      <usgs>193.149871826</usgs>
    </waypoint>
    <waypoint id='12572'>
      <lat>29.720173</lat>
      <lon>-98.121319</lon>
      <ele>191.4</ele>
      <usgs>194.657699585</usgs>
    </waypoint>
    <waypoint id='12571'>
      <lat>29.719882</lat>
      <lon>-98.12163</lon>
      <ele>191.9</ele>
      <usgs>195.450576782</usgs>
    </waypoint>
    <waypoint id='12570'>
      <lat>29.719812</lat>
      <lon>-98.12171</lon>
      <ele>192.4</ele>
      <usgs>195.67175293</usgs>
    </waypoint>
  </segment>

  <turn id='29'>
    <fromto>Torrey St. to Lakeview Blvd.</fromto>
    <cue>RIGHT onto Lakeview Blvd.</cue>
    <comments></comments>
  </turn>

  <segment id='29'>
    <road>Lakeview Blvd.</road>
    <fromto>Central Ave. to River Rd.</fromto>
    <comments>Austin St. becomes Lakeview Blvd. at the 90 degree left
    turn.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='1603'>
      <lat>29.719747</lat>
      <lon>-98.121892</lon>
      <ele>197.2</ele>
      <usgs>195.958282471</usgs>
    </waypoint>
    <waypoint id='1604'>
      <lat>29.720012</lat>
      <lon>-98.12219</lon>
      <ele>196.2</ele>
      <usgs>196.145446777</usgs>
    </waypoint>
    <waypoint id='1605'>
      <lat>29.720308</lat>
      <lon>-98.122555</lon>
      <ele>197.2</ele>
      <usgs>196.094863892</usgs>
    </waypoint>
    <waypoint id='1606'>
      <lat>29.720546</lat>
      <lon>-98.12282</lon>
      <ele>197.2</ele>
      <usgs>195.82774353</usgs>
    </waypoint>
    <waypoint id='1607'>
      <lat>29.720639</lat>
      <lon>-98.122913</lon>
      <ele>196.2</ele>
      <usgs>195.522445679</usgs>
    </waypoint>
    <waypoint id='1608'>
      <lat>29.720936</lat>
      <lon>-98.123209</lon>
      <ele>194.3</ele>
      <usgs>192.128967285</usgs>
    </waypoint>
    <waypoint id='1609'>
      <lat>29.721231</lat>
      <lon>-98.123538</lon>
      <ele>194.3</ele>
      <usgs>192.214294434</usgs>
    </waypoint>
    <waypoint id='1610'>
      <lat>29.721358</lat>
      <lon>-98.123689</lon>
      <ele>194.3</ele>
      <usgs>192.225799561</usgs>
    </waypoint>
  </segment>

  <turn id='30'>
    <fromto>Lakeview Blvd. to River Rd.</fromto>
    <cue>RIGHT onto River Rd.</cue>
    <comments></comments>
  </turn>

  <segment id='30'>
    <road>River Rd.</road>
    <fromto>Lakeview Blvd. to River Rd.</fromto>
    <comments>Wind past a creek, some fields, then some industrial stuff on the
      left.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='1611'>
      <lat>29.721548</lat>
      <lon>-98.123727</lon>
      <ele>193.8</ele>
      <usgs>192.250473022</usgs>
    </waypoint>
    <waypoint id='1612'>
      <lat>29.721634</lat>
      <lon>-98.123649</lon>
      <ele>194.3</ele>
      <usgs>192.206634521</usgs>
    </waypoint>
    <waypoint id='1613'>
      <lat>29.721816</lat>
      <lon>-98.123441</lon>
      <ele>193.4</ele>
      <usgs>192.130279541</usgs>
    </waypoint>
    <waypoint id='1614'>
      <lat>29.722001</lat>
      <lon>-98.123384</lon>
      <ele>192.9</ele>
      <usgs>192.259368896</usgs>
    </waypoint>
    <waypoint id='1615'>
      <lat>29.722061</lat>
      <lon>-98.123408</lon>
      <ele>192.4</ele>
      <usgs>192.346633911</usgs>
    </waypoint>
    <waypoint id='1616'>
      <lat>29.722445</lat>
      <lon>-98.123557</lon>
      <ele>193.4</ele>
      <usgs>192.318557739</usgs>
    </waypoint>
    <waypoint id='1617'>
      <lat>29.722882</lat>
      <lon>-98.123561</lon>
      <ele>194.3</ele>
      <usgs>192.431655884</usgs>
    </waypoint>
    <waypoint id='1618'>
      <lat>29.723284</lat>
      <lon>-98.123562</lon>
      <ele>195.3</ele>
      <usgs>192.485107422</usgs>
    </waypoint>
    <waypoint id='1619'>
      <lat>29.723703</lat>
      <lon>-98.123647</lon>
      <ele>195.3</ele>
      <usgs>192.502532959</usgs>
    </waypoint>
    <waypoint id='1620'>
      <lat>29.724349</lat>
      <lon>-98.123811</lon>
      <ele>195.8</ele>
      <usgs>193.088912964</usgs>
    </waypoint>
    <waypoint id='1621'>
      <lat>29.724873</lat>
      <lon>-98.123947</lon>
      <ele>196.7</ele>
      <usgs>194.296615601</usgs>
    </waypoint>
    <waypoint id='1622'>
      <lat>29.725348</lat>
      <lon>-98.124146</lon>
      <ele>195.3</ele>
      <usgs>193.966552734</usgs>
    </waypoint>
    <waypoint id='1623'>
      <lat>29.725881</lat>
      <lon>-98.124376</lon>
      <ele>195.3</ele>
      <usgs>193.761138916</usgs>
    </waypoint>
    <waypoint id='1624'>
      <lat>29.726208</lat>
      <lon>-98.12458</lon>
      <ele>196.7</ele>
      <usgs>194.523468018</usgs>
    </waypoint>
    <waypoint id='1625'>
      <lat>29.72656</lat>
      <lon>-98.124886</lon>
      <ele>196.2</ele>
      <usgs>194.785232544</usgs>
    </waypoint>
    <waypoint id='1626'>
      <lat>29.726867</lat>
      <lon>-98.125061</lon>
      <ele>196.7</ele>
      <usgs>195.644165039</usgs>
    </waypoint>
    <waypoint id='1627'>
      <lat>29.727382</lat>
      <lon>-98.125189</lon>
      <ele>198.2</ele>
      <usgs>197.249282837</usgs>
    </waypoint>
    <waypoint id='1628'>
      <lat>29.727778</lat>
      <lon>-98.125276</lon>
      <ele>200.1</ele>
      <usgs>198.570022583</usgs>
    </waypoint>
    <waypoint id='1629'>
      <lat>29.728259</lat>
      <lon>-98.125352</lon>
      <ele>203.5</ele>
      <usgs>201.136322021</usgs>
    </waypoint>
    <waypoint id='1630'>
      <lat>29.728622</lat>
      <lon>-98.125412</lon>
      <ele>204.9</ele>
      <usgs>202.82975769</usgs>
    </waypoint>
    <waypoint id='1631'>
      <lat>29.728866</lat>
      <lon>-98.125444</lon>
      <ele>205.4</ele>
      <usgs>203.515670776</usgs>
    </waypoint>
    <waypoint id='1632'>
      <lat>29.72895</lat>
      <lon>-98.125438</lon>
      <ele>205.9</ele>
      <usgs>203.816345215</usgs>
    </waypoint>
    <waypoint id='1633'>
      <lat>29.728968</lat>
      <lon>-98.125438</lon>
      <ele>205.9</ele>
      <usgs>203.816345215</usgs>
    </waypoint>
    <waypoint id='1634'>
      <lat>29.728978</lat>
      <lon>-98.125438</lon>
      <ele>205.4</ele>
      <usgs>203.816345215</usgs>
    </waypoint>
  </segment>

  <turn id='31'>
    <fromto>River Rd. to River Rd.</fromto>
    <cue>STRAIGHT on River Rd. (through the light)</cue>
    <comments>When River Rd. crosses over Loop 337, the speed changes and the
      traffic increaes majorly.</comments>
  </turn>

  <segment id='31'>
    <road>River Rd.</road>
    <fromto>River Rd. to River Rd.</fromto>
    <comments>Wind past a few buildings, but mostly fields.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>40</speed>
    <waypoint id='1635'>
      <lat>29.729098</lat>
      <lon>-98.125455</lon>
      <ele>205.9</ele>
      <usgs>204.159454346</usgs>
    </waypoint>
    <waypoint id='1636' stop='3'>
      <lat>29.729346</lat>
      <lon>-98.125501</lon>
      <ele>206.3</ele>
      <usgs>205.69543457</usgs>
    </waypoint>
    <waypoint id='1637'>
      <lat>29.729733</lat>
      <lon>-98.125559</lon>
      <ele>207.8</ele>
      <usgs>205.702957153</usgs>
    </waypoint>
    <waypoint id='1638'>
      <lat>29.730116</lat>
      <lon>-98.125617</lon>
      <ele>207.8</ele>
      <usgs>205.280776978</usgs>
    </waypoint>
    <waypoint id='1639'>
      <lat>29.730565</lat>
      <lon>-98.125732</lon>
      <ele>208.3</ele>
      <usgs>205.697387695</usgs>
    </waypoint>
    <waypoint id='1640'>
      <lat>29.73094</lat>
      <lon>-98.125925</lon>
      <ele>206.8</ele>
      <usgs>206.300033569</usgs>
    </waypoint>
    <waypoint id='1641'>
      <lat>29.73141</lat>
      <lon>-98.126274</lon>
      <ele>206.8</ele>
      <usgs>204.685913086</usgs>
    </waypoint>
    <waypoint id='1642'>
      <lat>29.731951</lat>
      <lon>-98.126688</lon>
      <ele>205.4</ele>
      <usgs>202.567398071</usgs>
    </waypoint>
    <waypoint id='1643'>
      <lat>29.732289</lat>
      <lon>-98.126962</lon>
      <ele>203.9</ele>
      <usgs>200.545043945</usgs>
    </waypoint>
    <waypoint id='1644'>
      <lat>29.732807</lat>
      <lon>-98.127374</lon>
      <ele>203.9</ele>
      <usgs>200.108673096</usgs>
    </waypoint>
    <waypoint id='1645'>
      <lat>29.733146</lat>
      <lon>-98.127637</lon>
      <ele>204.4</ele>
      <usgs>201.328933716</usgs>
    </waypoint>
    <waypoint id='1646'>
      <lat>29.733514</lat>
      <lon>-98.127928</lon>
      <ele>204.9</ele>
      <usgs>202.914398193</usgs>
    </waypoint>
    <waypoint id='1647'>
      <lat>29.733932</lat>
      <lon>-98.128258</lon>
      <ele>207.8</ele>
      <usgs>206.290237427</usgs>
    </waypoint>
    <waypoint id='1648'>
      <lat>29.734186</lat>
      <lon>-98.128446</lon>
      <ele>209.7</ele>
      <usgs>210.865142822</usgs>
    </waypoint>
    <waypoint id='1649'>
      <lat>29.734296</lat>
      <lon>-98.128534</lon>
      <ele>211.1</ele>
      <usgs>211.603713989</usgs>
    </waypoint>
    <waypoint id='1650'>
      <lat>29.734712</lat>
      <lon>-98.128864</lon>
      <ele>213.1</ele>
      <usgs>214.183990479</usgs>
    </waypoint>
    <waypoint id='1651'>
      <lat>29.73517</lat>
      <lon>-98.129219</lon>
      <ele>215.5</ele>
      <usgs>216.888900757</usgs>
    </waypoint>
    <waypoint id='1652'>
      <lat>29.735638</lat>
      <lon>-98.129562</lon>
      <ele>217.9</ele>
      <usgs>219.785507202</usgs>
    </waypoint>
    <waypoint id='1653'>
      <lat>29.736131</lat>
      <lon>-98.129882</lon>
      <ele>220.8</ele>
      <usgs>222.839691162</usgs>
    </waypoint>
    <waypoint id='1654'>
      <lat>29.736627</lat>
      <lon>-98.130161</lon>
      <ele>222.2</ele>
      <usgs>225.029434204</usgs>
    </waypoint>
    <waypoint id='1655'>
      <lat>29.736911</lat>
      <lon>-98.130307</lon>
      <ele>224.1</ele>
      <usgs>225.984725952</usgs>
    </waypoint>
    <waypoint id='1656'>
      <lat>29.737381</lat>
      <lon>-98.130535</lon>
      <ele>227.5</ele>
      <usgs>228.496246338</usgs>
    </waypoint>
    <waypoint id='1657'>
      <lat>29.737844</lat>
      <lon>-98.13076</lon>
      <ele>228.0</ele>
      <usgs>229.170028687</usgs>
    </waypoint>
    <waypoint id='1658'>
      <lat>29.738301</lat>
      <lon>-98.130986</lon>
      <ele>228.9</ele>
      <usgs>231.092025757</usgs>
    </waypoint>
    <waypoint id='1659'>
      <lat>29.738383</lat>
      <lon>-98.131025</lon>
      <ele>229.4</ele>
      <usgs>231.254898071</usgs>
    </waypoint>
    <waypoint id='1660'>
      <lat>29.738906</lat>
      <lon>-98.131277</lon>
      <ele>228.9</ele>
      <usgs>230.147857666</usgs>
    </waypoint>
    <waypoint id='1661'>
      <lat>29.739325</lat>
      <lon>-98.131495</lon>
      <ele>228.5</ele>
      <usgs>228.894317627</usgs>
    </waypoint>
    <waypoint id='1662'>
      <lat>29.739662</lat>
      <lon>-98.13171</lon>
      <ele>227.0</ele>
      <usgs>227.841644287</usgs>
    </waypoint>
    <waypoint id='1663'>
      <lat>29.739992</lat>
      <lon>-98.131968</lon>
      <ele>226.5</ele>
      <usgs>226.860733032</usgs>
    </waypoint>
    <waypoint id='1664'>
      <lat>29.740508</lat>
      <lon>-98.132512</lon>
      <ele>226.0</ele>
      <usgs>226.052032471</usgs>
    </waypoint>
    <waypoint id='1665'>
      <lat>29.740858</lat>
      <lon>-98.13302</lon>
      <ele>226.0</ele>
      <usgs>227.206832886</usgs>
    </waypoint>
    <waypoint id='1666'>
      <lat>29.741111</lat>
      <lon>-98.133467</lon>
      <ele>228.0</ele>
      <usgs>229.321960449</usgs>
    </waypoint>
    <waypoint id='1667'>
      <lat>29.7414</lat>
      <lon>-98.134018</lon>
      <ele>228.9</ele>
      <usgs>231.465057373</usgs>
    </waypoint>
    <waypoint id='1668'>
      <lat>29.741667</lat>
      <lon>-98.134529</lon>
      <ele>228.5</ele>
      <usgs>230.593032837</usgs>
    </waypoint>
    <waypoint id='1669'>
      <lat>29.74196</lat>
      <lon>-98.135104</lon>
      <ele>228.0</ele>
      <usgs>228.754486084</usgs>
    </waypoint>
    <waypoint id='1670'>
      <lat>29.742423</lat>
      <lon>-98.135998</lon>
      <ele>225.6</ele>
      <usgs>226.519515991</usgs>
    </waypoint>
    <waypoint id='1671'>
      <lat>29.742503</lat>
      <lon>-98.13615</lon>
      <ele>225.1</ele>
      <usgs>226.331237793</usgs>
    </waypoint>
    <waypoint id='1672'>
      <lat>29.742965</lat>
      <lon>-98.137024</lon>
      <ele>223.6</ele>
      <usgs>224.279037476</usgs>
    </waypoint>
    <waypoint id='1673'>
      <lat>29.743372</lat>
      <lon>-98.137792</lon>
      <ele>222.7</ele>
      <usgs>224.381347656</usgs>
    </waypoint>
    <waypoint id='1674'>
      <lat>29.743622</lat>
      <lon>-98.138238</lon>
      <ele>223.2</ele>
      <usgs>225.476425171</usgs>
    </waypoint>
    <waypoint id='1675'>
      <lat>29.743956</lat>
      <lon>-98.13887</lon>
      <ele>224.6</ele>
      <usgs>226.979888916</usgs>
    </waypoint>
    <waypoint id='1676'>
      <lat>29.744228</lat>
      <lon>-98.13938</lon>
      <ele>226.0</ele>
      <usgs>229.008621216</usgs>
    </waypoint>
    <waypoint id='1677'>
      <lat>29.744487</lat>
      <lon>-98.139873</lon>
      <ele>228.9</ele>
      <usgs>231.081512451</usgs>
    </waypoint>
    <waypoint id='1678'>
      <lat>29.744684</lat>
      <lon>-98.140262</lon>
      <ele>230.9</ele>
      <usgs>231.86781311</usgs>
    </waypoint>
    <waypoint id='1679'>
      <lat>29.744984</lat>
      <lon>-98.140881</lon>
      <ele>231.3</ele>
      <usgs>232.381637573</usgs>
    </waypoint>
    <waypoint id='1680'>
      <lat>29.74521</lat>
      <lon>-98.141444</lon>
      <ele>230.9</ele>
      <usgs>231.043746948</usgs>
    </waypoint>
    <waypoint id='1681'>
      <lat>29.745454</lat>
      <lon>-98.142164</lon>
      <ele>231.3</ele>
      <usgs>231.851974487</usgs>
    </waypoint>
    <waypoint id='1682'>
      <lat>29.745616</lat>
      <lon>-98.142649</lon>
      <ele>233.7</ele>
      <usgs>234.46572876</usgs>
    </waypoint>
    <waypoint id='1683'>
      <lat>29.745774</lat>
      <lon>-98.143139</lon>
      <ele>234.2</ele>
      <usgs>237.111312866</usgs>
    </waypoint>
    <waypoint id='1684'>
      <lat>29.745956</lat>
      <lon>-98.143709</lon>
      <ele>235.7</ele>
      <usgs>237.358184814</usgs>
    </waypoint>
    <waypoint id='1685'>
      <lat>29.746158</lat>
      <lon>-98.144311</lon>
      <ele>236.1</ele>
      <usgs>236.611373901</usgs>
    </waypoint>
    <waypoint id='1686'>
      <lat>29.74638</lat>
      <lon>-98.144774</lon>
      <ele>234.7</ele>
      <usgs>235.145050049</usgs>
    </waypoint>
    <waypoint id='1687'>
      <lat>29.746651</lat>
      <lon>-98.145064</lon>
      <ele>234.2</ele>
      <usgs>234.247467041</usgs>
    </waypoint>
    <waypoint id='1688'>
      <lat>29.746807</lat>
      <lon>-98.145188</lon>
      <ele>234.2</ele>
      <usgs>234.449432373</usgs>
    </waypoint>
  </segment>

  <turn id='32'>
    <fromto>River Rd. to River Rd.</fromto>
    <cue>RIGHT onto River Rd.</cue>
    <comments>At the 'Y', River Rd. goes to the right and Hueco Springs Loop
      Rd. goes to the left.  The River Rd. Icehouse is on the
      corner.</comments>
  </turn>

  <segment id='32'>
    <road>River Rd.</road>
    <fromto>River Rd. to Sattler Rd.</fromto>
    <comments>This is a very interesting road.  It's the heart of the Guadalupe
      River tubing area.  It winds along the river, past a multitude of
      campgrounds and tubing companies.  It crosses the river four
      times. </comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>30</speed>
    <waypoint id='1689' stop='5'>
      <lat>29.747092</lat>
      <lon>-98.14526</lon>
      <ele>232.8</ele>
      <usgs>235.081283569</usgs>
    </waypoint>
    <waypoint id='1690'>
      <lat>29.747244</lat>
      <lon>-98.145194</lon>
      <ele>233.7</ele>
      <usgs>235.798553467</usgs>
    </waypoint>
    <waypoint id='1691'>
      <lat>29.747688</lat>
      <lon>-98.144841</lon>
      <ele>233.3</ele>
      <usgs>236.677871704</usgs>
    </waypoint>
    <waypoint id='1692'>
      <lat>29.748075</lat>
      <lon>-98.144574</lon>
      <ele>233.3</ele>
      <usgs>234.890106201</usgs>
    </waypoint>
    <waypoint id='1693'>
      <lat>29.748573</lat>
      <lon>-98.144326</lon>
      <ele>233.3</ele>
      <usgs>232.753067017</usgs>
    </waypoint>
    <waypoint id='1694'>
      <lat>29.748807</lat>
      <lon>-98.144254</lon>
      <ele>232.8</ele>
      <usgs>231.240509033</usgs>
    </waypoint>
    <waypoint id='1695'>
      <lat>29.749222</lat>
      <lon>-98.144271</lon>
      <ele>232.3</ele>
      <usgs>230.444564819</usgs>
    </waypoint>
    <waypoint id='1696'>
      <lat>29.749462</lat>
      <lon>-98.144309</lon>
      <ele>230.9</ele>
      <usgs>229.61038208</usgs>
    </waypoint>
    <waypoint id='1697'>
      <lat>29.750107</lat>
      <lon>-98.144416</lon>
      <ele>228.0</ele>
      <usgs>225.306137085</usgs>
    </waypoint>
    <waypoint id='1698'>
      <lat>29.750533</lat>
      <lon>-98.144479</lon>
      <ele>226.5</ele>
      <usgs>223.755737305</usgs>
    </waypoint>
    <waypoint id='1699'>
      <lat>29.751017</lat>
      <lon>-98.144537</lon>
      <ele>227.0</ele>
      <usgs>224.251998901</usgs>
    </waypoint>
    <waypoint id='1700'>
      <lat>29.751488</lat>
      <lon>-98.144525</lon>
      <ele>225.6</ele>
      <usgs>224.520492554</usgs>
    </waypoint>
    <waypoint id='1701'>
      <lat>29.752036</lat>
      <lon>-98.144354</lon>
      <ele>225.1</ele>
      <usgs>224.444793701</usgs>
    </waypoint>
    <waypoint id='1702'>
      <lat>29.752582</lat>
      <lon>-98.144025</lon>
      <ele>224.6</ele>
      <usgs>222.932174683</usgs>
    </waypoint>
    <waypoint id='1703'>
      <lat>29.75281</lat>
      <lon>-98.143883</lon>
      <ele>222.7</ele>
      <usgs>220.968414307</usgs>
    </waypoint>
    <waypoint id='1704'>
      <lat>29.753223</lat>
      <lon>-98.143613</lon>
      <ele>221.2</ele>
      <usgs>219.460189819</usgs>
    </waypoint>
    <waypoint id='1705'>
      <lat>29.753604</lat>
      <lon>-98.143181</lon>
      <ele>218.8</ele>
      <usgs>214.319381714</usgs>
    </waypoint>
    <waypoint id='1706'>
      <lat>29.753761</lat>
      <lon>-98.142973</lon>
      <ele>217.9</ele>
      <usgs>213.57182312</usgs>
    </waypoint>
    <waypoint id='1707'>
      <lat>29.754014</lat>
      <lon>-98.142638</lon>
      <ele>215.5</ele>
      <usgs>213.394378662</usgs>
    </waypoint>
    <waypoint id='1708'>
      <lat>29.754193</lat>
      <lon>-98.142411</lon>
      <ele>213.1</ele>
      <usgs>212.396682739</usgs>
    </waypoint>
    <waypoint id='1709'>
      <lat>29.754662</lat>
      <lon>-98.141909</lon>
      <ele>211.6</ele>
      <usgs>209.893783569</usgs>
    </waypoint>
    <waypoint id='1710'>
      <lat>29.754959</lat>
      <lon>-98.141614</lon>
      <ele>210.2</ele>
      <usgs>208.855010986</usgs>
    </waypoint>
    <waypoint id='1711'>
      <lat>29.755443</lat>
      <lon>-98.141146</lon>
      <ele>207.3</ele>
      <usgs>206.551010132</usgs>
    </waypoint>
    <waypoint id='1712'>
      <lat>29.755534</lat>
      <lon>-98.141054</lon>
      <ele>207.3</ele>
      <usgs>206.252807617</usgs>
    </waypoint>
    <waypoint id='1713'>
      <lat>29.75581</lat>
      <lon>-98.140606</lon>
      <ele>205.9</ele>
      <usgs>202.603118896</usgs>
    </waypoint>
    <waypoint id='1714'>
      <lat>29.755908</lat>
      <lon>-98.140181</lon>
      <ele>202.5</ele>
      <usgs>199.225708008</usgs>
    </waypoint>
    <waypoint id='1715'>
      <lat>29.755947</lat>
      <lon>-98.139882</lon>
      <ele>202.0</ele>
      <usgs>196.404144287</usgs>
    </waypoint>
    <waypoint id='1716'>
      <lat>29.756091</lat>
      <lon>-98.139505</lon>
      <ele>201.1</ele>
      <usgs>194.534713745</usgs>
    </waypoint>
    <waypoint id='1717'>
      <lat>29.756277</lat>
      <lon>-98.139376</lon>
      <ele>199.6</ele>
      <usgs>195.297790527</usgs>
    </waypoint>
    <waypoint id='1718'>
      <lat>29.756488</lat>
      <lon>-98.139355</lon>
      <ele>199.6</ele>
      <usgs>195.360580444</usgs>
    </waypoint>
    <waypoint id='1719'>
      <lat>29.756684</lat>
      <lon>-98.139415</lon>
      <ele>199.1</ele>
      <usgs>195.390426636</usgs>
    </waypoint>
    <waypoint id='1720'>
      <lat>29.75736</lat>
      <lon>-98.13977</lon>
      <ele>202.0</ele>
      <usgs>196.19329834</usgs>
    </waypoint>
    <waypoint id='1721'>
      <lat>29.757786</lat>
      <lon>-98.139983</lon>
      <ele>203.0</ele>
      <usgs>196.832458496</usgs>
    </waypoint>
    <waypoint id='1722'>
      <lat>29.758376</lat>
      <lon>-98.140223</lon>
      <ele>202.5</ele>
      <usgs>197.76512146</usgs>
    </waypoint>
    <waypoint id='1723'>
      <lat>29.758813</lat>
      <lon>-98.140316</lon>
      <ele>202.0</ele>
      <usgs>198.455657959</usgs>
    </waypoint>
    <waypoint id='1724'>
      <lat>29.759207</lat>
      <lon>-98.140299</lon>
      <ele>201.1</ele>
      <usgs>198.600921631</usgs>
    </waypoint>
    <waypoint id='1725'>
      <lat>29.759761</lat>
      <lon>-98.140215</lon>
      <ele>201.5</ele>
      <usgs>197.834777832</usgs>
    </waypoint>
    <waypoint id='1726'>
      <lat>29.760376</lat>
      <lon>-98.140115</lon>
      <ele>201.5</ele>
      <usgs>196.430435181</usgs>
    </waypoint>
    <waypoint id='1727'>
      <lat>29.760807</lat>
      <lon>-98.140125</lon>
      <ele>200.1</ele>
      <usgs>195.855117798</usgs>
    </waypoint>
    <waypoint id='1728'>
      <lat>29.761337</lat>
      <lon>-98.140271</lon>
      <ele>201.5</ele>
      <usgs>196.469039917</usgs>
    </waypoint>
    <waypoint id='1729'>
      <lat>29.762037</lat>
      <lon>-98.140464</lon>
      <ele>201.5</ele>
      <usgs>199.633102417</usgs>
    </waypoint>
    <waypoint id='1730' stop='6'>
      <lat>29.762472</lat>
      <lon>-98.140618</lon>
      <ele>201.5</ele>
      <usgs>199.409042358</usgs>
    </waypoint>
    <waypoint id='1731'>
      <lat>29.762813</lat>
      <lon>-98.14077</lon>
      <ele>202.5</ele>
      <usgs>199.67288208</usgs>
    </waypoint>
    <waypoint id='1732'>
      <lat>29.763453</lat>
      <lon>-98.141108</lon>
      <ele>202.5</ele>
      <usgs>199.631774902</usgs>
    </waypoint>
    <waypoint id='1733'>
      <lat>29.763979</lat>
      <lon>-98.141451</lon>
      <ele>202.5</ele>
      <usgs>199.949081421</usgs>
    </waypoint>
    <waypoint id='1734'>
      <lat>29.764386</lat>
      <lon>-98.141729</lon>
      <ele>202.5</ele>
      <usgs>198.467147827</usgs>
    </waypoint>
    <waypoint id='1735'>
      <lat>29.764621</lat>
      <lon>-98.141897</lon>
      <ele>202.0</ele>
      <usgs>197.546401978</usgs>
    </waypoint>
    <waypoint id='1736'>
      <lat>29.7649</lat>
      <lon>-98.141977</lon>
      <ele>201.5</ele>
      <usgs>194.979034424</usgs>
    </waypoint>
    <waypoint id='1737'>
      <lat>29.765626</lat>
      <lon>-98.141938</lon>
      <ele>202.5</ele>
      <usgs>196.441390991</usgs>
    </waypoint>
    <waypoint id='1738' poi='2'>
      <lat>29.765761</lat>
      <lon>-98.141938</lon>
      <ele>202.0</ele>
      <usgs>198.820846558</usgs>
    </waypoint>
    <waypoint id='1739'>
      <lat>29.765984</lat>
      <lon>-98.142074</lon>
      <ele>202.0</ele>
      <usgs>200.475021362</usgs>
    </waypoint>
    <waypoint id='1740'>
      <lat>29.766046</lat>
      <lon>-98.142207</lon>
      <ele>201.5</ele>
      <usgs>202.284805298</usgs>
    </waypoint>
    <waypoint id='1741'>
      <lat>29.766267</lat>
      <lon>-98.142891</lon>
      <ele>200.6</ele>
      <usgs>202.823165894</usgs>
    </waypoint>
    <waypoint id='1742'>
      <lat>29.766432</lat>
      <lon>-98.143422</lon>
      <ele>201.5</ele>
      <usgs>203.472595215</usgs>
    </waypoint>
    <waypoint id='1743'>
      <lat>29.766571</lat>
      <lon>-98.143868</lon>
      <ele>202.0</ele>
      <usgs>202.977905273</usgs>
    </waypoint>
    <waypoint id='1744'>
      <lat>29.766726</lat>
      <lon>-98.144384</lon>
      <ele>202.5</ele>
      <usgs>204.122406006</usgs>
    </waypoint>
    <waypoint id='1745'>
      <lat>29.766818</lat>
      <lon>-98.144752</lon>
      <ele>202.0</ele>
      <usgs>204.767059326</usgs>
    </waypoint>
    <waypoint id='1746'>
      <lat>29.766851</lat>
      <lon>-98.144974</lon>
      <ele>202.5</ele>
      <usgs>204.492233276</usgs>
    </waypoint>
    <waypoint id='1747'>
      <lat>29.766839</lat>
      <lon>-98.145627</lon>
      <ele>202.0</ele>
      <usgs>203.965682983</usgs>
    </waypoint>
    <waypoint id='1748'>
      <lat>29.766817</lat>
      <lon>-98.146391</lon>
      <ele>201.1</ele>
      <usgs>203.464614868</usgs>
    </waypoint>
    <waypoint id='1749'>
      <lat>29.76679</lat>
      <lon>-98.147213</lon>
      <ele>201.5</ele>
      <usgs>203.157653809</usgs>
    </waypoint>
    <waypoint id='1750'>
      <lat>29.766727</lat>
      <lon>-98.147755</lon>
      <ele>201.5</ele>
      <usgs>203.03163147</usgs>
    </waypoint>
    <waypoint id='1751'>
      <lat>29.766611</lat>
      <lon>-98.148364</lon>
      <ele>201.1</ele>
      <usgs>203.078414917</usgs>
    </waypoint>
    <waypoint id='1752'>
      <lat>29.766499</lat>
      <lon>-98.14889</lon>
      <ele>201.1</ele>
      <usgs>203.208496094</usgs>
    </waypoint>
    <waypoint id='1753'>
      <lat>29.766299</lat>
      <lon>-98.149474</lon>
      <ele>202.0</ele>
      <usgs>203.039794922</usgs>
    </waypoint>
    <waypoint id='1754'>
      <lat>29.76616</lat>
      <lon>-98.149912</lon>
      <ele>201.5</ele>
      <usgs>202.891403198</usgs>
    </waypoint>
    <waypoint id='1755'>
      <lat>29.766026</lat>
      <lon>-98.150333</lon>
      <ele>202.5</ele>
      <usgs>203.09173584</usgs>
    </waypoint>
    <waypoint id='1756'>
      <lat>29.765837</lat>
      <lon>-98.150876</lon>
      <ele>202.0</ele>
      <usgs>203.332580566</usgs>
    </waypoint>
    <waypoint id='1757'>
      <lat>29.76552</lat>
      <lon>-98.151783</lon>
      <ele>202.5</ele>
      <usgs>202.857421875</usgs>
    </waypoint>
    <waypoint id='1758'>
      <lat>29.765297</lat>
      <lon>-98.152418</lon>
      <ele>203.0</ele>
      <usgs>203.285873413</usgs>
    </waypoint>
    <waypoint id='1759'>
      <lat>29.765012</lat>
      <lon>-98.153279</lon>
      <ele>203.9</ele>
      <usgs>203.905273438</usgs>
    </waypoint>
    <waypoint id='1760'>
      <lat>29.76476</lat>
      <lon>-98.15409</lon>
      <ele>203.9</ele>
      <usgs>204.670196533</usgs>
    </waypoint>
    <waypoint id='1761'>
      <lat>29.764584</lat>
      <lon>-98.154841</lon>
      <ele>204.4</ele>
      <usgs>205.03414917</usgs>
    </waypoint>
    <waypoint id='1762'>
      <lat>29.764555</lat>
      <lon>-98.155408</lon>
      <ele>204.4</ele>
      <usgs>205.423736572</usgs>
    </waypoint>
    <waypoint id='1763'>
      <lat>29.764621</lat>
      <lon>-98.156196</lon>
      <ele>203.0</ele>
      <usgs>204.843307495</usgs>
    </waypoint>
    <waypoint id='1764'>
      <lat>29.764684</lat>
      <lon>-98.156823</lon>
      <ele>203.5</ele>
      <usgs>204.568511963</usgs>
    </waypoint>
    <waypoint id='1765'>
      <lat>29.764749</lat>
      <lon>-98.157105</lon>
      <ele>203.0</ele>
      <usgs>204.755950928</usgs>
    </waypoint>
    <waypoint id='1766'>
      <lat>29.764932</lat>
      <lon>-98.157453</lon>
      <ele>203.0</ele>
      <usgs>204.665664673</usgs>
    </waypoint>
    <waypoint id='1767'>
      <lat>29.765265</lat>
      <lon>-98.157884</lon>
      <ele>203.0</ele>
      <usgs>203.267089844</usgs>
    </waypoint>
    <waypoint id='1768'>
      <lat>29.765658</lat>
      <lon>-98.158192</lon>
      <ele>202.5</ele>
      <usgs>204.173309326</usgs>
    </waypoint>
    <waypoint id='1769'>
      <lat>29.766159</lat>
      <lon>-98.158425</lon>
      <ele>203.0</ele>
      <usgs>204.911727905</usgs>
    </waypoint>
    <waypoint id='1770'>
      <lat>29.766678</lat>
      <lon>-98.158549</lon>
      <ele>202.5</ele>
      <usgs>204.629806519</usgs>
    </waypoint>
    <waypoint id='1771'>
      <lat>29.767288</lat>
      <lon>-98.158584</lon>
      <ele>203.5</ele>
      <usgs>205.542602539</usgs>
    </waypoint>
    <waypoint id='1772'>
      <lat>29.767902</lat>
      <lon>-98.158562</lon>
      <ele>202.5</ele>
      <usgs>205.660903931</usgs>
    </waypoint>
    <waypoint id='1773'>
      <lat>29.768694</lat>
      <lon>-98.158457</lon>
      <ele>203.0</ele>
      <usgs>208.104187012</usgs>
    </waypoint>
    <waypoint id='1774'>
      <lat>29.769426</lat>
      <lon>-98.158384</lon>
      <ele>202.5</ele>
      <usgs>207.960830688</usgs>
    </waypoint>
    <waypoint id='1775'>
      <lat>29.76986</lat>
      <lon>-98.158387</lon>
      <ele>202.0</ele>
      <usgs>205.723556519</usgs>
    </waypoint>
    <waypoint id='1776'>
      <lat>29.770559</lat>
      <lon>-98.158366</lon>
      <ele>202.5</ele>
      <usgs>203.895767212</usgs>
    </waypoint>
    <waypoint id='1777'>
      <lat>29.771054</lat>
      <lon>-98.158332</lon>
      <ele>203.0</ele>
      <usgs>206.059539795</usgs>
    </waypoint>
    <waypoint id='1778' stop='7'>
      <lat>29.771681</lat>
      <lon>-98.158337</lon>
      <ele>203.0</ele>
      <usgs>204.326950073</usgs>
    </waypoint>
    <waypoint id='1779'>
      <lat>29.772307</lat>
      <lon>-98.158402</lon>
      <ele>202.5</ele>
      <usgs>204.360122681</usgs>
    </waypoint>
    <waypoint id='1780'>
      <lat>29.773154</lat>
      <lon>-98.15852</lon>
      <ele>203.0</ele>
      <usgs>200.731506348</usgs>
    </waypoint>
    <waypoint id='1781'>
      <lat>29.773724</lat>
      <lon>-98.158646</lon>
      <ele>203.5</ele>
      <usgs>204.605361938</usgs>
    </waypoint>
    <waypoint id='1782'>
      <lat>29.774368</lat>
      <lon>-98.158837</lon>
      <ele>204.4</ele>
      <usgs>209.201797485</usgs>
    </waypoint>
    <waypoint id='1783'>
      <lat>29.775006</lat>
      <lon>-98.159009</lon>
      <ele>205.9</ele>
      <usgs>209.970352173</usgs>
    </waypoint>
    <waypoint id='1784'>
      <lat>29.775649</lat>
      <lon>-98.159206</lon>
      <ele>206.8</ele>
      <usgs>206.977325439</usgs>
    </waypoint>
    <waypoint id='1785'>
      <lat>29.776317</lat>
      <lon>-98.159431</lon>
      <ele>205.9</ele>
      <usgs>205.014556885</usgs>
    </waypoint>
    <waypoint id='1786'>
      <lat>29.776909</lat>
      <lon>-98.159644</lon>
      <ele>205.9</ele>
      <usgs>205.253219604</usgs>
    </waypoint>
    <waypoint id='1787'>
      <lat>29.777555</lat>
      <lon>-98.159843</lon>
      <ele>204.4</ele>
      <usgs>205.904556274</usgs>
    </waypoint>
    <waypoint id='1788'>
      <lat>29.778079</lat>
      <lon>-98.159883</lon>
      <ele>203.9</ele>
      <usgs>206.23526001</usgs>
    </waypoint>
    <waypoint id='1789'>
      <lat>29.778679</lat>
      <lon>-98.15985</lon>
      <ele>203.9</ele>
      <usgs>205.800003052</usgs>
    </waypoint>
    <waypoint id='1790' poi='3'>
      <lat>29.778891</lat>
      <lon>-98.159789</lon>
      <ele>204.9</ele>
      <usgs>206.232345581</usgs>
    </waypoint>
    <waypoint id='1791'>
      <lat>29.779142</lat>
      <lon>-98.159862</lon>
      <ele>204.4</ele>
      <usgs>205.303268433</usgs>
    </waypoint>
    <waypoint id='1792'>
      <lat>29.779185</lat>
      <lon>-98.159916</lon>
      <ele>204.4</ele>
      <usgs>204.622970581</usgs>
    </waypoint>
    <waypoint id='1793'>
      <lat>29.779483</lat>
      <lon>-98.160422</lon>
      <ele>205.9</ele>
      <usgs>203.422561646</usgs>
    </waypoint>
    <waypoint id='1794'>
      <lat>29.779651</lat>
      <lon>-98.160578</lon>
      <ele>206.3</ele>
      <usgs>210.644683838</usgs>
    </waypoint>
    <waypoint id='1795'>
      <lat>29.779812</lat>
      <lon>-98.160547</lon>
      <ele>207.8</ele>
      <usgs>209.943664551</usgs>
    </waypoint>
    <waypoint id='1796'>
      <lat>29.7803</lat>
      <lon>-98.16024</lon>
      <ele>208.7</ele>
      <usgs>215.370758057</usgs>
    </waypoint>
    <waypoint id='1797'>
      <lat>29.780686</lat>
      <lon>-98.159995</lon>
      <ele>208.7</ele>
      <usgs>215.201019287</usgs>
    </waypoint>
    <waypoint id='1798'>
      <lat>29.781039</lat>
      <lon>-98.159753</lon>
      <ele>210.2</ele>
      <usgs>215.330047607</usgs>
    </waypoint>
    <waypoint id='1799'>
      <lat>29.781385</lat>
      <lon>-98.1595</lon>
      <ele>211.6</ele>
      <usgs>213.195785522</usgs>
    </waypoint>
    <waypoint id='1800'>
      <lat>29.781628</lat>
      <lon>-98.1593</lon>
      <ele>212.1</ele>
      <usgs>213.710327148</usgs>
    </waypoint>
    <waypoint id='1801'>
      <lat>29.781991</lat>
      <lon>-98.158931</lon>
      <ele>212.6</ele>
      <usgs>214.281677246</usgs>
    </waypoint>
    <waypoint id='1802'>
      <lat>29.782436</lat>
      <lon>-98.158445</lon>
      <ele>214.0</ele>
      <usgs>215.847061157</usgs>
    </waypoint>
    <waypoint id='1803'>
      <lat>29.78272</lat>
      <lon>-98.158058</lon>
      <ele>215.0</ele>
      <usgs>213.693328857</usgs>
    </waypoint>
    <waypoint id='1804'>
      <lat>29.782875</lat>
      <lon>-98.157704</lon>
      <ele>215.5</ele>
      <usgs>213.053710938</usgs>
    </waypoint>
    <waypoint id='1805'>
      <lat>29.783112</lat>
      <lon>-98.15712</lon>
      <ele>214.0</ele>
      <usgs>212.11517334</usgs>
    </waypoint>
    <waypoint id='1806'>
      <lat>29.783349</lat>
      <lon>-98.156486</lon>
      <ele>214.5</ele>
      <usgs>212.568527222</usgs>
    </waypoint>
    <waypoint id='1807'>
      <lat>29.783586</lat>
      <lon>-98.155817</lon>
      <ele>213.1</ele>
      <usgs>211.452804565</usgs>
    </waypoint>
    <waypoint id='1808'>
      <lat>29.78391</lat>
      <lon>-98.154903</lon>
      <ele>213.1</ele>
      <usgs>212.055267334</usgs>
    </waypoint>
    <waypoint id='1809'>
      <lat>29.784089</lat>
      <lon>-98.15427</lon>
      <ele>211.1</ele>
      <usgs>211.38331604</usgs>
    </waypoint>
    <waypoint id='1810'>
      <lat>29.784304</lat>
      <lon>-98.153813</lon>
      <ele>211.1</ele>
      <usgs>210.765563965</usgs>
    </waypoint>
    <waypoint id='1811'>
      <lat>29.78465</lat>
      <lon>-98.153276</lon>
      <ele>209.7</ele>
      <usgs>210.464584351</usgs>
    </waypoint>
    <waypoint id='1812'>
      <lat>29.785072</lat>
      <lon>-98.152748</lon>
      <ele>208.3</ele>
      <usgs>208.182601929</usgs>
    </waypoint>
    <waypoint id='1813'>
      <lat>29.785561</lat>
      <lon>-98.152316</lon>
      <ele>209.2</ele>
      <usgs>207.02696228</usgs>
    </waypoint>
    <waypoint id='1814'>
      <lat>29.786153</lat>
      <lon>-98.151917</lon>
      <ele>209.2</ele>
      <usgs>206.509490967</usgs>
    </waypoint>
    <waypoint id='1815'>
      <lat>29.786626</lat>
      <lon>-98.151669</lon>
      <ele>206.8</ele>
      <usgs>205.260040283</usgs>
    </waypoint>
    <waypoint id='1816'>
      <lat>29.78716</lat>
      <lon>-98.151522</lon>
      <ele>205.4</ele>
      <usgs>205.184112549</usgs>
    </waypoint>
    <waypoint id='1817'>
      <lat>29.787591</lat>
      <lon>-98.151512</lon>
      <ele>206.8</ele>
      <usgs>205.428009033</usgs>
    </waypoint>
    <waypoint id='1818'>
      <lat>29.788234</lat>
      <lon>-98.151627</lon>
      <ele>206.3</ele>
      <usgs>205.742034912</usgs>
    </waypoint>
    <waypoint id='1819'>
      <lat>29.788716</lat>
      <lon>-98.151787</lon>
      <ele>207.3</ele>
      <usgs>206.344589233</usgs>
    </waypoint>
    <waypoint id='1820'>
      <lat>29.789123</lat>
      <lon>-98.151938</lon>
      <ele>208.7</ele>
      <usgs>207.310195923</usgs>
    </waypoint>
    <waypoint id='1821'>
      <lat>29.789563</lat>
      <lon>-98.152099</lon>
      <ele>210.2</ele>
      <usgs>208.372497559</usgs>
    </waypoint>
    <waypoint id='1822'>
      <lat>29.789955</lat>
      <lon>-98.152201</lon>
      <ele>211.1</ele>
      <usgs>208.986846924</usgs>
    </waypoint>
    <waypoint id='1823'>
      <lat>29.790513</lat>
      <lon>-98.152276</lon>
      <ele>212.1</ele>
      <usgs>209.853897095</usgs>
    </waypoint>
    <waypoint id='1824'>
      <lat>29.790913</lat>
      <lon>-98.152284</lon>
      <ele>211.6</ele>
      <usgs>209.951248169</usgs>
    </waypoint>
    <waypoint id='1825'>
      <lat>29.791416</lat>
      <lon>-98.152247</lon>
      <ele>212.1</ele>
      <usgs>210.230056763</usgs>
    </waypoint>
    <waypoint id='1826'>
      <lat>29.791773</lat>
      <lon>-98.152196</lon>
      <ele>210.2</ele>
      <usgs>209.437988281</usgs>
    </waypoint>
    <waypoint id='1827'>
      <lat>29.792235</lat>
      <lon>-98.152072</lon>
      <ele>209.2</ele>
      <usgs>209.179244995</usgs>
    </waypoint>
    <waypoint id='1828'>
      <lat>29.792721</lat>
      <lon>-98.151925</lon>
      <ele>209.2</ele>
      <usgs>208.379669189</usgs>
    </waypoint>
    <waypoint id='1829'>
      <lat>29.793216</lat>
      <lon>-98.151773</lon>
      <ele>210.7</ele>
      <usgs>208.677307129</usgs>
    </waypoint>
    <waypoint id='1830'>
      <lat>29.793602</lat>
      <lon>-98.151658</lon>
      <ele>212.1</ele>
      <usgs>208.390914917</usgs>
    </waypoint>
    <waypoint id='1831'>
      <lat>29.793983</lat>
      <lon>-98.15144</lon>
      <ele>212.6</ele>
      <usgs>208.602233887</usgs>
    </waypoint>
    <waypoint id='1832'>
      <lat>29.794646</lat>
      <lon>-98.150997</lon>
      <ele>212.6</ele>
      <usgs>209.212478638</usgs>
    </waypoint>
    <waypoint id='1833'>
      <lat>29.7951</lat>
      <lon>-98.150602</lon>
      <ele>212.6</ele>
      <usgs>209.412231445</usgs>
    </waypoint>
    <waypoint id='1834' stop='8'>
      <lat>29.795614</lat>
      <lon>-98.150138</lon>
      <ele>212.6</ele>
      <usgs>209.167785645</usgs>
    </waypoint>
    <waypoint id='1835'>
      <lat>29.796245</lat>
      <lon>-98.149623</lon>
      <ele>212.6</ele>
      <usgs>209.43586731</usgs>
    </waypoint>
    <waypoint id='1836'>
      <lat>29.796669</lat>
      <lon>-98.149356</lon>
      <ele>212.1</ele>
      <usgs>210.780014038</usgs>
    </waypoint>
    <waypoint id='1837'>
      <lat>29.797171</lat>
      <lon>-98.149112</lon>
      <ele>212.6</ele>
      <usgs>211.425292969</usgs>
    </waypoint>
    <waypoint id='1838'>
      <lat>29.797629</lat>
      <lon>-98.148944</lon>
      <ele>213.1</ele>
      <usgs>212.843688965</usgs>
    </waypoint>
    <waypoint id='1839'>
      <lat>29.798231</lat>
      <lon>-98.148779</lon>
      <ele>214.0</ele>
      <usgs>213.600219727</usgs>
    </waypoint>
    <waypoint id='1840'>
      <lat>29.798411</lat>
      <lon>-98.14875</lon>
      <ele>215.5</ele>
      <usgs>213.559295654</usgs>
    </waypoint>
    <waypoint id='1841'>
      <lat>29.798642</lat>
      <lon>-98.148772</lon>
      <ele>215.5</ele>
      <usgs>213.427490234</usgs>
    </waypoint>
    <waypoint id='1842'>
      <lat>29.79921</lat>
      <lon>-98.148927</lon>
      <ele>216.4</ele>
      <usgs>217.771102905</usgs>
    </waypoint>
    <waypoint id='1843'>
      <lat>29.799273</lat>
      <lon>-98.148928</lon>
      <ele>216.9</ele>
      <usgs>218.057510376</usgs>
    </waypoint>
    <waypoint id='1844'>
      <lat>29.799512</lat>
      <lon>-98.148877</lon>
      <ele>217.4</ele>
      <usgs>218.074005127</usgs>
    </waypoint>
    <waypoint id='1845'>
      <lat>29.799754</lat>
      <lon>-98.148701</lon>
      <ele>218.4</ele>
      <usgs>218.058898926</usgs>
    </waypoint>
    <waypoint id='1846'>
      <lat>29.800086</lat>
      <lon>-98.148294</lon>
      <ele>220.3</ele>
      <usgs>219.27507019</usgs>
    </waypoint>
    <waypoint id='1847'>
      <lat>29.800362</lat>
      <lon>-98.148054</lon>
      <ele>220.8</ele>
      <usgs>218.733963013</usgs>
    </waypoint>
    <waypoint id='1848'>
      <lat>29.80073</lat>
      <lon>-98.147891</lon>
      <ele>219.3</ele>
      <usgs>218.782775879</usgs>
    </waypoint>
    <waypoint id='1849'>
      <lat>29.80115</lat>
      <lon>-98.14784</lon>
      <ele>218.8</ele>
      <usgs>218.418319702</usgs>
    </waypoint>
    <waypoint id='1850'>
      <lat>29.801634</lat>
      <lon>-98.147898</lon>
      <ele>218.8</ele>
      <usgs>218.634521484</usgs>
    </waypoint>
    <waypoint id='1851'>
      <lat>29.802111</lat>
      <lon>-98.14804</lon>
      <ele>218.4</ele>
      <usgs>218.306167603</usgs>
    </waypoint>
    <waypoint id='1852'>
      <lat>29.802508</lat>
      <lon>-98.148289</lon>
      <ele>217.9</ele>
      <usgs>218.079315186</usgs>
    </waypoint>
    <waypoint id='1853'>
      <lat>29.802812</lat>
      <lon>-98.148543</lon>
      <ele>217.9</ele>
      <usgs>218.122665405</usgs>
    </waypoint>
    <waypoint id='1854'>
      <lat>29.802968</lat>
      <lon>-98.148719</lon>
      <ele>217.9</ele>
      <usgs>218.011642456</usgs>
    </waypoint>
    <waypoint id='1855'>
      <lat>29.803198</lat>
      <lon>-98.149131</lon>
      <ele>217.4</ele>
      <usgs>218.206741333</usgs>
    </waypoint>
    <waypoint id='1856'>
      <lat>29.803453</lat>
      <lon>-98.149733</lon>
      <ele>218.4</ele>
      <usgs>218.779205322</usgs>
    </waypoint>
    <waypoint id='1857'>
      <lat>29.803617</lat>
      <lon>-98.150109</lon>
      <ele>218.4</ele>
      <usgs>219.718505859</usgs>
    </waypoint>
    <waypoint id='1858'>
      <lat>29.803786</lat>
      <lon>-98.150562</lon>
      <ele>218.4</ele>
      <usgs>221.147201538</usgs>
    </waypoint>
    <waypoint id='1859'>
      <lat>29.803936</lat>
      <lon>-98.151058</lon>
      <ele>218.8</ele>
      <usgs>220.727478027</usgs>
    </waypoint>
    <waypoint id='1860'>
      <lat>29.804052</lat>
      <lon>-98.15166</lon>
      <ele>219.3</ele>
      <usgs>221.325790405</usgs>
    </waypoint>
    <waypoint id='1861'>
      <lat>29.804144</lat>
      <lon>-98.152223</lon>
      <ele>219.3</ele>
      <usgs>222.031494141</usgs>
    </waypoint>
    <waypoint id='1862'>
      <lat>29.80423</lat>
      <lon>-98.152836</lon>
      <ele>220.3</ele>
      <usgs>221.802780151</usgs>
    </waypoint>
    <waypoint id='1863'>
      <lat>29.804271</lat>
      <lon>-98.153419</lon>
      <ele>220.8</ele>
      <usgs>221.235366821</usgs>
    </waypoint>
    <waypoint id='1864'>
      <lat>29.804313</lat>
      <lon>-98.154046</lon>
      <ele>220.3</ele>
      <usgs>221.565444946</usgs>
    </waypoint>
    <waypoint id='1865'>
      <lat>29.804374</lat>
      <lon>-98.154674</lon>
      <ele>220.8</ele>
      <usgs>220.920684814</usgs>
    </waypoint>
    <waypoint id='1866'>
      <lat>29.804449</lat>
      <lon>-98.155229</lon>
      <ele>221.7</ele>
      <usgs>220.338378906</usgs>
    </waypoint>
    <waypoint id='1867'>
      <lat>29.804506</lat>
      <lon>-98.155852</lon>
      <ele>222.7</ele>
      <usgs>221.144180298</usgs>
    </waypoint>
    <waypoint id='1868'>
      <lat>29.804551</lat>
      <lon>-98.156288</lon>
      <ele>222.7</ele>
      <usgs>221.132644653</usgs>
    </waypoint>
    <waypoint id='1869'>
      <lat>29.80471</lat>
      <lon>-98.157037</lon>
      <ele>222.2</ele>
      <usgs>221.427078247</usgs>
    </waypoint>
    <waypoint id='1870'>
      <lat>29.804928</lat>
      <lon>-98.157466</lon>
      <ele>221.7</ele>
      <usgs>219.669784546</usgs>
    </waypoint>
    <waypoint id='1871'>
      <lat>29.805136</lat>
      <lon>-98.157933</lon>
      <ele>218.8</ele>
      <usgs>214.331634521</usgs>
    </waypoint>
    <waypoint id='1872'>
      <lat>29.80517</lat>
      <lon>-98.158033</lon>
      <ele>218.8</ele>
      <usgs>214.80960083</usgs>
    </waypoint>
    <waypoint id='1873'>
      <lat>29.805204</lat>
      <lon>-98.158419</lon>
      <ele>220.8</ele>
      <usgs>218.591323853</usgs>
    </waypoint>
    <waypoint id='1874'>
      <lat>29.805162</lat>
      <lon>-98.158601</lon>
      <ele>220.3</ele>
      <usgs>219.876815796</usgs>
    </waypoint>
    <waypoint id='1875'>
      <lat>29.804894</lat>
      <lon>-98.159272</lon>
      <ele>221.2</ele>
      <usgs>221.319107056</usgs>
    </waypoint>
    <waypoint id='1876'>
      <lat>29.804643</lat>
      <lon>-98.159892</lon>
      <ele>221.7</ele>
      <usgs>222.042419434</usgs>
    </waypoint>
    <waypoint id='1877'>
      <lat>29.804491</lat>
      <lon>-98.160428</lon>
      <ele>222.2</ele>
      <usgs>222.806671143</usgs>
    </waypoint>
    <waypoint id='1878'>
      <lat>29.80448</lat>
      <lon>-98.16084</lon>
      <ele>223.2</ele>
      <usgs>221.899810791</usgs>
    </waypoint>
    <waypoint id='1879'>
      <lat>29.804474</lat>
      <lon>-98.16111</lon>
      <ele>221.7</ele>
      <usgs>221.410202026</usgs>
    </waypoint>
    <waypoint id='1880'>
      <lat>29.804402</lat>
      <lon>-98.161675</lon>
      <ele>220.3</ele>
      <usgs>220.619415283</usgs>
    </waypoint>
    <waypoint id='1881'>
      <lat>29.804239</lat>
      <lon>-98.162279</lon>
      <ele>220.3</ele>
      <usgs>218.155136108</usgs>
    </waypoint>
    <waypoint id='1882'>
      <lat>29.803978</lat>
      <lon>-98.162846</lon>
      <ele>218.8</ele>
      <usgs>216.797088623</usgs>
    </waypoint>
    <waypoint id='1883'>
      <lat>29.803805</lat>
      <lon>-98.163107</lon>
      <ele>216.9</ele>
      <usgs>214.79989624</usgs>
    </waypoint>
    <waypoint id='1884'>
      <lat>29.803697</lat>
      <lon>-98.163441</lon>
      <ele>215.5</ele>
      <usgs>208.773452759</usgs>
    </waypoint>
    <waypoint id='1885'>
      <lat>29.803694</lat>
      <lon>-98.163566</lon>
      <ele>216.4</ele>
      <usgs>208.892684937</usgs>
    </waypoint>
    <waypoint id='1886' poi='4'>
      <lat>29.803692</lat>
      <lon>-98.163941</lon>
      <ele>215.0</ele>
      <usgs>210.641815186</usgs>
    </waypoint>
    <waypoint id='1887'>
      <lat>29.80368</lat>
      <lon>-98.164305</lon>
      <ele>213.6</ele>
      <usgs>212.271469116</usgs>
    </waypoint>
    <waypoint id='1888'>
      <lat>29.803592</lat>
      <lon>-98.164751</lon>
      <ele>214.0</ele>
      <usgs>213.253616333</usgs>
    </waypoint>
    <waypoint id='1889'>
      <lat>29.803378</lat>
      <lon>-98.165225</lon>
      <ele>216.0</ele>
      <usgs>214.005935669</usgs>
    </waypoint>
    <waypoint id='1890'>
      <lat>29.803229</lat>
      <lon>-98.165491</lon>
      <ele>217.4</ele>
      <usgs>214.139205933</usgs>
    </waypoint>
    <waypoint id='1891'>
      <lat>29.802991</lat>
      <lon>-98.165871</lon>
      <ele>217.9</ele>
      <usgs>214.438934326</usgs>
    </waypoint>
    <waypoint id='1892'>
      <lat>29.802702</lat>
      <lon>-98.16634</lon>
      <ele>218.4</ele>
      <usgs>214.566558838</usgs>
    </waypoint>
    <waypoint id='1893'>
      <lat>29.802361</lat>
      <lon>-98.166895</lon>
      <ele>219.3</ele>
      <usgs>214.606735229</usgs>
    </waypoint>
    <waypoint id='1894'>
      <lat>29.802016</lat>
      <lon>-98.16742</lon>
      <ele>219.3</ele>
      <usgs>214.661956787</usgs>
    </waypoint>
    <waypoint id='1895'>
      <lat>29.801768</lat>
      <lon>-98.167859</lon>
      <ele>217.9</ele>
      <usgs>214.861434937</usgs>
    </waypoint>
    <waypoint id='1896'>
      <lat>29.801676</lat>
      <lon>-98.168058</lon>
      <ele>219.3</ele>
      <usgs>215.134475708</usgs>
    </waypoint>
    <waypoint id='1897'>
      <lat>29.80149</lat>
      <lon>-98.168627</lon>
      <ele>219.8</ele>
      <usgs>215.707733154</usgs>
    </waypoint>
    <waypoint id='1898'>
      <lat>29.801362</lat>
      <lon>-98.16928</lon>
      <ele>220.8</ele>
      <usgs>216.151596069</usgs>
    </waypoint>
    <waypoint id='1899'>
      <lat>29.80133</lat>
      <lon>-98.169861</lon>
      <ele>221.7</ele>
      <usgs>216.905105591</usgs>
    </waypoint>
    <waypoint id='1900'>
      <lat>29.801297</lat>
      <lon>-98.170476</lon>
      <ele>221.2</ele>
      <usgs>217.306442261</usgs>
    </waypoint>
    <waypoint id='1901'>
      <lat>29.801315</lat>
      <lon>-98.170905</lon>
      <ele>221.2</ele>
      <usgs>217.092575073</usgs>
    </waypoint>
    <waypoint id='1902'>
      <lat>29.801477</lat>
      <lon>-98.171295</lon>
      <ele>220.8</ele>
      <usgs>217.176864624</usgs>
    </waypoint>
    <waypoint id='1903'>
      <lat>29.801579</lat>
      <lon>-98.171416</lon>
      <ele>220.8</ele>
      <usgs>218.004119873</usgs>
    </waypoint>
    <waypoint id='1904'>
      <lat>29.802108</lat>
      <lon>-98.171852</lon>
      <ele>221.2</ele>
      <usgs>218.99458313</usgs>
    </waypoint>
    <waypoint id='1905'>
      <lat>29.802732</lat>
      <lon>-98.172348</lon>
      <ele>220.8</ele>
      <usgs>219.377151489</usgs>
    </waypoint>
    <waypoint id='1906'>
      <lat>29.803057</lat>
      <lon>-98.172621</lon>
      <ele>219.8</ele>
      <usgs>218.012649536</usgs>
    </waypoint>
    <waypoint id='1907'>
      <lat>29.803414</lat>
      <lon>-98.172877</lon>
      <ele>217.9</ele>
      <usgs>213.014205933</usgs>
    </waypoint>
    <waypoint id='1908'>
      <lat>29.803857</lat>
      <lon>-98.173101</lon>
      <ele>214.5</ele>
      <usgs>213.051376343</usgs>
    </waypoint>
    <waypoint id='1909'>
      <lat>29.804046</lat>
      <lon>-98.173165</lon>
      <ele>214.0</ele>
      <usgs>212.787384033</usgs>
    </waypoint>
    <waypoint id='1910'>
      <lat>29.804671</lat>
      <lon>-98.173316</lon>
      <ele>213.6</ele>
      <usgs>218.227722168</usgs>
    </waypoint>
    <waypoint id='1911'>
      <lat>29.805143</lat>
      <lon>-98.173362</lon>
      <ele>214.5</ele>
      <usgs>219.702270508</usgs>
    </waypoint>
    <waypoint id='1912'>
      <lat>29.805625</lat>
      <lon>-98.173352</lon>
      <ele>215.0</ele>
      <usgs>223.104797363</usgs>
    </waypoint>
    <waypoint id='1913'>
      <lat>29.806286</lat>
      <lon>-98.173226</lon>
      <ele>214.0</ele>
      <usgs>225.333068848</usgs>
    </waypoint>
    <waypoint id='1914'>
      <lat>29.806954</lat>
      <lon>-98.173091</lon>
      <ele>213.1</ele>
      <usgs>223.827865601</usgs>
    </waypoint>
    <waypoint id='1915'>
      <lat>29.807469</lat>
      <lon>-98.172912</lon>
      <ele>212.6</ele>
      <usgs>223.221389771</usgs>
    </waypoint>
    <waypoint id='1916'>
      <lat>29.807838</lat>
      <lon>-98.172837</lon>
      <ele>213.1</ele>
      <usgs>213.327270508</usgs>
    </waypoint>
    <waypoint id='1917'>
      <lat>29.808341</lat>
      <lon>-98.172914</lon>
      <ele>213.1</ele>
      <usgs>226.029220581</usgs>
    </waypoint>
    <waypoint id='1918'>
      <lat>29.808718</lat>
      <lon>-98.173131</lon>
      <ele>213.1</ele>
      <usgs>231.385437012</usgs>
    </waypoint>
    <waypoint id='1919'>
      <lat>29.809066</lat>
      <lon>-98.173408</lon>
      <ele>213.1</ele>
      <usgs>219.130767822</usgs>
    </waypoint>
    <waypoint id='1920'>
      <lat>29.809329</lat>
      <lon>-98.173525</lon>
      <ele>215.0</ele>
      <usgs>217.850662231</usgs>
    </waypoint>
    <waypoint id='1921'>
      <lat>29.809482</lat>
      <lon>-98.17358</lon>
      <ele>217.4</ele>
      <usgs>219.820236206</usgs>
    </waypoint>
    <waypoint id='1922'>
      <lat>29.809924</lat>
      <lon>-98.173703</lon>
      <ele>219.8</ele>
      <usgs>225.284835815</usgs>
    </waypoint>
    <waypoint id='1923'>
      <lat>29.810265</lat>
      <lon>-98.173816</lon>
      <ele>220.8</ele>
      <usgs>224.636627197</usgs>
    </waypoint>
    <waypoint id='1924'>
      <lat>29.810764</lat>
      <lon>-98.173951</lon>
      <ele>223.2</ele>
      <usgs>224.977920532</usgs>
    </waypoint>
    <waypoint id='1925'>
      <lat>29.811207</lat>
      <lon>-98.174089</lon>
      <ele>224.6</ele>
      <usgs>225.227798462</usgs>
    </waypoint>
    <waypoint id='1926'>
      <lat>29.811657</lat>
      <lon>-98.174298</lon>
      <ele>224.6</ele>
      <usgs>225.320724487</usgs>
    </waypoint>
    <waypoint id='1927'>
      <lat>29.812168</lat>
      <lon>-98.174612</lon>
      <ele>226.0</ele>
      <usgs>228.242874146</usgs>
    </waypoint>
    <waypoint id='1928'>
      <lat>29.812597</lat>
      <lon>-98.174878</lon>
      <ele>226.0</ele>
      <usgs>228.970794678</usgs>
    </waypoint>
    <waypoint id='1929'>
      <lat>29.813256</lat>
      <lon>-98.175291</lon>
      <ele>226.0</ele>
      <usgs>228.938980103</usgs>
    </waypoint>
    <waypoint id='1930'>
      <lat>29.813843</lat>
      <lon>-98.175621</lon>
      <ele>226.5</ele>
      <usgs>228.592330933</usgs>
    </waypoint>
    <waypoint id='1931'>
      <lat>29.814187</lat>
      <lon>-98.175648</lon>
      <ele>227.5</ele>
      <usgs>229.198532104</usgs>
    </waypoint>
    <waypoint id='1932'>
      <lat>29.814606</lat>
      <lon>-98.175525</lon>
      <ele>226.5</ele>
      <usgs>229.894439697</usgs>
    </waypoint>
    <waypoint id='1933'>
      <lat>29.815042</lat>
      <lon>-98.175287</lon>
      <ele>228.0</ele>
      <usgs>229.988235474</usgs>
    </waypoint>
    <waypoint id='1934'>
      <lat>29.815399</lat>
      <lon>-98.175053</lon>
      <ele>230.9</ele>
      <usgs>230.882003784</usgs>
    </waypoint>
    <waypoint id='1935'>
      <lat>29.815694</lat>
      <lon>-98.174863</lon>
      <ele>229.9</ele>
      <usgs>231.063308716</usgs>
    </waypoint>
    <waypoint id='1936'>
      <lat>29.816295</lat>
      <lon>-98.174387</lon>
      <ele>229.9</ele>
      <usgs>231.039581299</usgs>
    </waypoint>
    <waypoint id='1937'>
      <lat>29.816737</lat>
      <lon>-98.173938</lon>
      <ele>230.4</ele>
      <usgs>230.967468262</usgs>
    </waypoint>
    <waypoint id='1938'>
      <lat>29.817078</lat>
      <lon>-98.173557</lon>
      <ele>230.4</ele>
      <usgs>230.747177124</usgs>
    </waypoint>
    <waypoint id='1939'>
      <lat>29.817436</lat>
      <lon>-98.173276</lon>
      <ele>229.9</ele>
      <usgs>230.120452881</usgs>
    </waypoint>
    <waypoint id='1940'>
      <lat>29.817997</lat>
      <lon>-98.172947</lon>
      <ele>228.9</ele>
      <usgs>228.611038208</usgs>
    </waypoint>
    <waypoint id='1941'>
      <lat>29.818076</lat>
      <lon>-98.172907</lon>
      <ele>228.5</ele>
      <usgs>228.048797607</usgs>
    </waypoint>
    <waypoint id='1942'>
      <lat>29.818296</lat>
      <lon>-98.172719</lon>
      <ele>226.5</ele>
      <usgs>226.845092773</usgs>
    </waypoint>
    <waypoint id='1943'>
      <lat>29.818423</lat>
      <lon>-98.172418</lon>
      <ele>225.1</ele>
      <usgs>226.557800293</usgs>
    </waypoint>
    <waypoint id='1944'>
      <lat>29.81844</lat>
      <lon>-98.172189</lon>
      <ele>225.6</ele>
      <usgs>221.705993652</usgs>
    </waypoint>
    <waypoint id='1945'>
      <lat>29.818446</lat>
      <lon>-98.171746</lon>
      <ele>225.1</ele>
      <usgs>223.37298584</usgs>
    </waypoint>
    <waypoint id='1946'>
      <lat>29.818608</lat>
      <lon>-98.171149</lon>
      <ele>223.2</ele>
      <usgs>221.762863159</usgs>
    </waypoint>
    <waypoint id='1947'>
      <lat>29.81878</lat>
      <lon>-98.170787</lon>
      <ele>220.8</ele>
      <usgs>221.286300659</usgs>
    </waypoint>
    <waypoint id='1948'>
      <lat>29.819054</lat>
      <lon>-98.170057</lon>
      <ele>219.3</ele>
      <usgs>222.427963257</usgs>
    </waypoint>
    <waypoint id='1949'>
      <lat>29.819294</lat>
      <lon>-98.169286</lon>
      <ele>218.8</ele>
      <usgs>222.325622559</usgs>
    </waypoint>
    <waypoint id='1950'>
      <lat>29.819571</lat>
      <lon>-98.168505</lon>
      <ele>217.9</ele>
      <usgs>222.584564209</usgs>
    </waypoint>
    <waypoint id='1951'>
      <lat>29.81983</lat>
      <lon>-98.168046</lon>
      <ele>220.3</ele>
      <usgs>220.8671875</usgs>
    </waypoint>
    <waypoint id='1952'>
      <lat>29.819954</lat>
      <lon>-98.167795</lon>
      <ele>221.7</ele>
      <usgs>220.847076416</usgs>
    </waypoint>
    <waypoint id='1953'>
      <lat>29.820188</lat>
      <lon>-98.167442</lon>
      <ele>224.1</ele>
      <usgs>221.254135132</usgs>
    </waypoint>
    <waypoint id='1954'>
      <lat>29.820421</lat>
      <lon>-98.167177</lon>
      <ele>226.0</ele>
      <usgs>222.574493408</usgs>
    </waypoint>
    <waypoint id='1955'>
      <lat>29.82081</lat>
      <lon>-98.166914</lon>
      <ele>226.5</ele>
      <usgs>222.621948242</usgs>
    </waypoint>
    <waypoint id='1956'>
      <lat>29.821199</lat>
      <lon>-98.166763</lon>
      <ele>226.0</ele>
      <usgs>223.748519897</usgs>
    </waypoint>
    <waypoint id='1957'>
      <lat>29.821657</lat>
      <lon>-98.166621</lon>
      <ele>226.0</ele>
      <usgs>225.924163818</usgs>
    </waypoint>
    <waypoint id='1958'>
      <lat>29.821792</lat>
      <lon>-98.166578</lon>
      <ele>224.6</ele>
      <usgs>225.964447021</usgs>
    </waypoint>
    <waypoint id='1959' stop='9'>
      <lat>29.822266</lat>
      <lon>-98.166435</lon>
      <ele>225.1</ele>
      <usgs>226.082504272</usgs>
    </waypoint>
    <waypoint id='1960'>
      <lat>29.822875</lat>
      <lon>-98.166246</lon>
      <ele>224.1</ele>
      <usgs>226.093444824</usgs>
    </waypoint>
    <waypoint id='1961'>
      <lat>29.823412</lat>
      <lon>-98.166074</lon>
      <ele>223.6</ele>
      <usgs>226.097183228</usgs>
    </waypoint>
    <waypoint id='1962'>
      <lat>29.824191</lat>
      <lon>-98.165818</lon>
      <ele>224.6</ele>
      <usgs>225.363250732</usgs>
    </waypoint>
    <waypoint id='1963'>
      <lat>29.824763</lat>
      <lon>-98.165609</lon>
      <ele>225.1</ele>
      <usgs>225.62272644</usgs>
    </waypoint>
    <waypoint id='1964'>
      <lat>29.825336</lat>
      <lon>-98.165397</lon>
      <ele>225.1</ele>
      <usgs>225.897842407</usgs>
    </waypoint>
    <waypoint id='1965'>
      <lat>29.826171</lat>
      <lon>-98.165093</lon>
      <ele>225.6</ele>
      <usgs>225.895172119</usgs>
    </waypoint>
    <waypoint id='1966'>
      <lat>29.826555</lat>
      <lon>-98.165051</lon>
      <ele>223.6</ele>
      <usgs>225.15083313</usgs>
    </waypoint>
    <waypoint id='1967'>
      <lat>29.826648</lat>
      <lon>-98.165047</lon>
      <ele>223.2</ele>
      <usgs>224.579391479</usgs>
    </waypoint>
    <waypoint id='1968'>
      <lat>29.827036</lat>
      <lon>-98.165132</lon>
      <ele>221.7</ele>
      <usgs>221.804519653</usgs>
    </waypoint>
    <waypoint id='1969'>
      <lat>29.8273</lat>
      <lon>-98.16522</lon>
      <ele>221.7</ele>
      <usgs>220.212249756</usgs>
    </waypoint>
    <waypoint id='1970'>
      <lat>29.827379</lat>
      <lon>-98.165233</lon>
      <ele>221.7</ele>
      <usgs>220.39541626</usgs>
    </waypoint>
    <waypoint id='1971'>
      <lat>29.827722</lat>
      <lon>-98.165185</lon>
      <ele>223.2</ele>
      <usgs>225.943389893</usgs>
    </waypoint>
    <waypoint id='1972'>
      <lat>29.828094</lat>
      <lon>-98.165065</lon>
      <ele>225.6</ele>
      <usgs>228.227157593</usgs>
    </waypoint>
    <waypoint id='1973'>
      <lat>29.82861</lat>
      <lon>-98.164943</lon>
      <ele>226.0</ele>
      <usgs>228.375991821</usgs>
    </waypoint>
    <waypoint id='1974'>
      <lat>29.829071</lat>
      <lon>-98.164866</lon>
      <ele>227.0</ele>
      <usgs>228.696777344</usgs>
    </waypoint>
    <waypoint id='1975'>
      <lat>29.82944</lat>
      <lon>-98.16469</lon>
      <ele>228.0</ele>
      <usgs>230.071578979</usgs>
    </waypoint>
    <waypoint id='1976'>
      <lat>29.829804</lat>
      <lon>-98.164426</lon>
      <ele>229.9</ele>
      <usgs>231.484161377</usgs>
    </waypoint>
    <waypoint id='1977'>
      <lat>29.830238</lat>
      <lon>-98.164071</lon>
      <ele>229.9</ele>
      <usgs>232.036773682</usgs>
    </waypoint>
    <waypoint id='1978'>
      <lat>29.830757</lat>
      <lon>-98.163653</lon>
      <ele>231.8</ele>
      <usgs>232.428878784</usgs>
    </waypoint>
    <waypoint id='1979'>
      <lat>29.831303</lat>
      <lon>-98.163209</lon>
      <ele>231.3</ele>
      <usgs>232.968582153</usgs>
    </waypoint>
    <waypoint id='1980'>
      <lat>29.831761</lat>
      <lon>-98.162894</lon>
      <ele>231.3</ele>
      <usgs>234.455734253</usgs>
    </waypoint>
    <waypoint id='1981'>
      <lat>29.83208</lat>
      <lon>-98.162805</lon>
      <ele>231.8</ele>
      <usgs>235.877624512</usgs>
    </waypoint>
    <waypoint id='1982'>
      <lat>29.832344</lat>
      <lon>-98.16284</lon>
      <ele>231.8</ele>
      <usgs>237.003616333</usgs>
    </waypoint>
    <waypoint id='1983'>
      <lat>29.832576</lat>
      <lon>-98.162952</lon>
      <ele>233.7</ele>
      <usgs>237.483016968</usgs>
    </waypoint>
    <waypoint id='1984'>
      <lat>29.832844</lat>
      <lon>-98.163156</lon>
      <ele>234.2</ele>
      <usgs>238.748794556</usgs>
    </waypoint>
    <waypoint id='1985'>
      <lat>29.833237</lat>
      <lon>-98.163549</lon>
      <ele>235.2</ele>
      <usgs>241.540740967</usgs>
    </waypoint>
    <waypoint id='1986'>
      <lat>29.833719</lat>
      <lon>-98.164032</lon>
      <ele>236.1</ele>
      <usgs>243.891891479</usgs>
    </waypoint>
    <waypoint id='1987'>
      <lat>29.834173</lat>
      <lon>-98.164415</lon>
      <ele>238.1</ele>
      <usgs>242.403335571</usgs>
    </waypoint>
    <waypoint id='1988'>
      <lat>29.834639</lat>
      <lon>-98.164745</lon>
      <ele>239.0</ele>
      <usgs>241.024688721</usgs>
    </waypoint>
    <waypoint id='1989'>
      <lat>29.835104</lat>
      <lon>-98.16498</lon>
      <ele>239.0</ele>
      <usgs>242.042831421</usgs>
    </waypoint>
    <waypoint id='1990'>
      <lat>29.83555</lat>
      <lon>-98.165083</lon>
      <ele>238.5</ele>
      <usgs>242.38369751</usgs>
    </waypoint>
    <waypoint id='1991'>
      <lat>29.835856</lat>
      <lon>-98.165031</lon>
      <ele>240.0</ele>
      <usgs>242.362731934</usgs>
    </waypoint>
    <waypoint id='1992'>
      <lat>29.836459</lat>
      <lon>-98.164795</lon>
      <ele>240.9</ele>
      <usgs>242.601074219</usgs>
    </waypoint>
    <waypoint id='1993'>
      <lat>29.836947</lat>
      <lon>-98.164608</lon>
      <ele>240.9</ele>
      <usgs>241.69569397</usgs>
    </waypoint>
    <waypoint id='1994'>
      <lat>29.837279</lat>
      <lon>-98.164596</lon>
      <ele>241.4</ele>
      <usgs>240.253677368</usgs>
    </waypoint>
    <waypoint id='1995'>
      <lat>29.837782</lat>
      <lon>-98.16471</lon>
      <ele>239.5</ele>
      <usgs>241.506774902</usgs>
    </waypoint>
    <waypoint id='1996'>
      <lat>29.838111</lat>
      <lon>-98.164912</lon>
      <ele>240.0</ele>
      <usgs>245.257247925</usgs>
    </waypoint>
    <waypoint id='1997'>
      <lat>29.838407</lat>
      <lon>-98.165229</lon>
      <ele>241.4</ele>
      <usgs>246.156723022</usgs>
    </waypoint>
    <waypoint id='1998'>
      <lat>29.838446</lat>
      <lon>-98.165287</lon>
      <ele>241.4</ele>
      <usgs>246.433502197</usgs>
    </waypoint>
    <waypoint id='1999'>
      <lat>29.838713</lat>
      <lon>-98.165748</lon>
      <ele>242.4</ele>
      <usgs>247.473403931</usgs>
    </waypoint>
    <waypoint id='2000'>
      <lat>29.83893</lat>
      <lon>-98.166159</lon>
      <ele>242.4</ele>
      <usgs>247.214019775</usgs>
    </waypoint>
    <waypoint id='2001'>
      <lat>29.839199</lat>
      <lon>-98.166626</lon>
      <ele>240.9</ele>
      <usgs>245.727859497</usgs>
    </waypoint>
    <waypoint id='2002'>
      <lat>29.839242</lat>
      <lon>-98.166699</lon>
      <ele>240.9</ele>
      <usgs>245.163009644</usgs>
    </waypoint>
    <waypoint id='2003'>
      <lat>29.839536</lat>
      <lon>-98.167186</lon>
      <ele>238.1</ele>
      <usgs>242.403366089</usgs>
    </waypoint>
    <waypoint id='2004'>
      <lat>29.839915</lat>
      <lon>-98.167715</lon>
      <ele>235.7</ele>
      <usgs>237.339797974</usgs>
    </waypoint>
    <waypoint id='2005'>
      <lat>29.840068</lat>
      <lon>-98.167887</lon>
      <ele>234.7</ele>
      <usgs>236.70300293</usgs>
    </waypoint>
    <waypoint id='2006'>
      <lat>29.840575</lat>
      <lon>-98.16835</lon>
      <ele>233.7</ele>
      <usgs>234.699417114</usgs>
    </waypoint>
    <waypoint id='2007'>
      <lat>29.840934</lat>
      <lon>-98.168612</lon>
      <ele>231.8</ele>
      <usgs>233.179214478</usgs>
    </waypoint>
    <waypoint id='2008'>
      <lat>29.84103</lat>
      <lon>-98.168662</lon>
      <ele>231.8</ele>
      <usgs>232.977035522</usgs>
    </waypoint>
    <waypoint id='2009'>
      <lat>29.841451</lat>
      <lon>-98.168695</lon>
      <ele>230.9</ele>
      <usgs>230.888793945</usgs>
    </waypoint>
    <waypoint id='2010'>
      <lat>29.841746</lat>
      <lon>-98.168553</lon>
      <ele>230.9</ele>
      <usgs>229.379104614</usgs>
    </waypoint>
    <waypoint id='2011'>
      <lat>29.84217</lat>
      <lon>-98.168196</lon>
      <ele>229.4</ele>
      <usgs>227.181991577</usgs>
    </waypoint>
    <waypoint id='2012'>
      <lat>29.84234</lat>
      <lon>-98.168042</lon>
      <ele>227.5</ele>
      <usgs>226.788101196</usgs>
    </waypoint>
    <waypoint id='2013'>
      <lat>29.842592</lat>
      <lon>-98.168005</lon>
      <ele>224.1</ele>
      <usgs>219.515701294</usgs>
    </waypoint>
    <waypoint id='2014' poi='5'>
      <lat>29.842732</lat>
      <lon>-98.168121</lon>
      <ele>223.2</ele>
      <usgs>219.468002319</usgs>
    </waypoint>
    <waypoint id='2015'>
      <lat>29.843077</lat>
      <lon>-98.168428</lon>
      <ele>222.2</ele>
      <usgs>224.395462036</usgs>
    </waypoint>
    <waypoint id='2016'>
      <lat>29.843207</lat>
      <lon>-98.168665</lon>
      <ele>226.0</ele>
      <usgs>225.862579346</usgs>
    </waypoint>
    <waypoint id='2017'>
      <lat>29.843218</lat>
      <lon>-98.168735</lon>
      <ele>226.5</ele>
      <usgs>226.139846802</usgs>
    </waypoint>
    <waypoint id='2018'>
      <lat>29.843279</lat>
      <lon>-98.169105</lon>
      <ele>228.0</ele>
      <usgs>226.709274292</usgs>
    </waypoint>
    <waypoint id='2019'>
      <lat>29.843457</lat>
      <lon>-98.169415</lon>
      <ele>228.5</ele>
      <usgs>226.97064209</usgs>
    </waypoint>
    <waypoint id='2020'>
      <lat>29.843499</lat>
      <lon>-98.169459</lon>
      <ele>228.5</ele>
      <usgs>226.742935181</usgs>
    </waypoint>
    <waypoint id='2021'>
      <lat>29.843789</lat>
      <lon>-98.169632</lon>
      <ele>229.4</ele>
      <usgs>226.784408569</usgs>
    </waypoint>
    <waypoint id='2022'>
      <lat>29.844233</lat>
      <lon>-98.16986</lon>
      <ele>230.4</ele>
      <usgs>227.539993286</usgs>
    </waypoint>
    <waypoint id='2023'>
      <lat>29.844794</lat>
      <lon>-98.170142</lon>
      <ele>230.9</ele>
      <usgs>227.944869995</usgs>
    </waypoint>
    <waypoint id='2024'>
      <lat>29.84523</lat>
      <lon>-98.170397</lon>
      <ele>231.3</ele>
      <usgs>230.143539429</usgs>
    </waypoint>
    <waypoint id='2025'>
      <lat>29.845699</lat>
      <lon>-98.170738</lon>
      <ele>231.3</ele>
      <usgs>232.278686523</usgs>
    </waypoint>
    <waypoint id='2026'>
      <lat>29.846173</lat>
      <lon>-98.171096</lon>
      <ele>232.3</ele>
      <usgs>233.024627686</usgs>
    </waypoint>
    <waypoint id='2027'>
      <lat>29.846682</lat>
      <lon>-98.171402</lon>
      <ele>233.3</ele>
      <usgs>233.976852417</usgs>
    </waypoint>
    <waypoint id='2028'>
      <lat>29.847185</lat>
      <lon>-98.171695</lon>
      <ele>233.3</ele>
      <usgs>235.076202393</usgs>
    </waypoint>
    <waypoint id='2029'>
      <lat>29.847498</lat>
      <lon>-98.171969</lon>
      <ele>232.8</ele>
      <usgs>235.459579468</usgs>
    </waypoint>
    <waypoint id='2030'>
      <lat>29.847794</lat>
      <lon>-98.172378</lon>
      <ele>234.7</ele>
      <usgs>235.907699585</usgs>
    </waypoint>
    <waypoint id='2031'>
      <lat>29.847975</lat>
      <lon>-98.172827</lon>
      <ele>234.7</ele>
      <usgs>236.033843994</usgs>
    </waypoint>
    <waypoint id='2032' stop='4'>
      <lat>29.848062</lat>
      <lon>-98.173359</lon>
      <ele>235.7</ele>
      <usgs>236.421813965</usgs>
    </waypoint>
  </segment>

  <turn id='34'>
    <fromto>River Rd. to Sattler Rd.</fromto>
    <cue>LEFT onto Sattler Rd.</cue>
    <comments>Sattler Rd. veers off to the left just before you get to FM
      2673.</comments>
  </turn>

  <segment id='34'>
    <road>Sattler Rd.</road>
    <fromto>River Rd. to Pecan Row</fromto>
    <comments>Go past a few businesses and the VFW hall.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>20</speed>
    <waypoint id='2033'>
      <lat>29.848092</lat>
      <lon>-98.173923</lon>
      <ele>236.6</ele>
      <usgs>236.647735596</usgs>
    </waypoint>
    <waypoint id='2082'>
      <lat>29.847996</lat>
      <lon>-98.174174</lon>
      <ele>237.1</ele>
      <usgs>236.73777771</usgs>
    </waypoint>
    <waypoint id='2083'>
      <lat>29.847974</lat>
      <lon>-98.174216</lon>
      <ele>236.6</ele>
      <usgs>236.73777771</usgs>
    </waypoint>
    <waypoint id='2084'>
      <lat>29.847781</lat>
      <lon>-98.174634</lon>
      <ele>237.1</ele>
      <usgs>237.12512207</usgs>
    </waypoint>
    <waypoint id='2085'>
      <lat>29.847558</lat>
      <lon>-98.175084</lon>
      <ele>238.5</ele>
      <usgs>237.335449219</usgs>
    </waypoint>
    <waypoint id='2086'>
      <lat>29.847427</lat>
      <lon>-98.175358</lon>
      <ele>238.5</ele>
      <usgs>237.617050171</usgs>
    </waypoint>
    <waypoint id='2087'>
      <lat>29.847339</lat>
      <lon>-98.175578</lon>
      <ele>238.1</ele>
      <usgs>238.063095093</usgs>
    </waypoint>
    <waypoint id='2088'>
      <lat>29.847222</lat>
      <lon>-98.175865</lon>
      <ele>238.5</ele>
      <usgs>238.417999268</usgs>
    </waypoint>
  </segment>

  <turn id='35'>
    <fromto>Sattler Rd. to Pecan Row</fromto>
    <cue>LEFT onto Pecan Row</cue>
    <comments>Pecan Row T's in on the left.</comments>
  </turn>

  <segment id='35'>
    <road>Pecan Row</road>
    <fromto>Sattler Rd. to Guadalupe Rd.</fromto>
    <comments>Go past some country houses.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='2089'>
      <lat>29.847137</lat>
      <lon>-98.176021</lon>
      <ele>239.0</ele>
      <usgs>238.540802002</usgs>
    </waypoint>
    <waypoint id='2090'>
      <lat>29.847008</lat>
      <lon>-98.176017</lon>
      <ele>239.5</ele>
      <usgs>238.387634277</usgs>
    </waypoint>
    <waypoint id='2091'>
      <lat>29.84694</lat>
      <lon>-98.175986</lon>
      <ele>240.5</ele>
      <usgs>238.310256958</usgs>
    </waypoint>
    <waypoint id='2092'>
      <lat>29.846631</lat>
      <lon>-98.175826</lon>
      <ele>240.0</ele>
      <usgs>237.776931763</usgs>
    </waypoint>
    <waypoint id='2093'>
      <lat>29.846349</lat>
      <lon>-98.175687</lon>
      <ele>239.5</ele>
      <usgs>237.512435913</usgs>
    </waypoint>
    <waypoint id='2094'>
      <lat>29.84595</lat>
      <lon>-98.175485</lon>
      <ele>240.0</ele>
      <usgs>237.158843994</usgs>
    </waypoint>
    <waypoint id='2095'>
      <lat>29.845622</lat>
      <lon>-98.175312</lon>
      <ele>238.5</ele>
      <usgs>236.683654785</usgs>
    </waypoint>
    <waypoint id='2096'>
      <lat>29.845356</lat>
      <lon>-98.175169</lon>
      <ele>239.5</ele>
      <usgs>236.158248901</usgs>
    </waypoint>
    <waypoint id='2097'>
      <lat>29.844973</lat>
      <lon>-98.174968</lon>
      <ele>237.6</ele>
      <usgs>235.523162842</usgs>
    </waypoint>
    <waypoint id='2098'>
      <lat>29.844666</lat>
      <lon>-98.174803</lon>
      <ele>236.6</ele>
      <usgs>234.897460938</usgs>
    </waypoint>
    <waypoint id='2099'>
      <lat>29.844288</lat>
      <lon>-98.174599</lon>
      <ele>238.5</ele>
      <usgs>234.249160767</usgs>
    </waypoint>
    <waypoint id='2100'>
      <lat>29.843819</lat>
      <lon>-98.174337</lon>
      <ele>239.5</ele>
      <usgs>233.587234497</usgs>
    </waypoint>
    <waypoint id='2101'>
      <lat>29.843692</lat>
      <lon>-98.174261</lon>
      <ele>237.6</ele>
      <usgs>233.426193237</usgs>
    </waypoint>
    <waypoint id='2102'>
      <lat>29.843358</lat>
      <lon>-98.174084</lon>
      <ele>236.1</ele>
      <usgs>233.099990845</usgs>
    </waypoint>
    <waypoint id='2103'>
      <lat>29.842933</lat>
      <lon>-98.173858</lon>
      <ele>234.2</ele>
      <usgs>232.866439819</usgs>
    </waypoint>
    <waypoint id='2104'>
      <lat>29.842406</lat>
      <lon>-98.173572</lon>
      <ele>232.3</ele>
      <usgs>232.660827637</usgs>
    </waypoint>
    <waypoint id='2105'>
      <lat>29.841925</lat>
      <lon>-98.173318</lon>
      <ele>232.3</ele>
      <usgs>232.519348145</usgs>
    </waypoint>
    <waypoint id='2106'>
      <lat>29.841308</lat>
      <lon>-98.172992</lon>
      <ele>232.3</ele>
      <usgs>232.093383789</usgs>
    </waypoint>
    <waypoint id='2107'>
      <lat>29.841071</lat>
      <lon>-98.172859</lon>
      <ele>231.3</ele>
      <usgs>231.822525024</usgs>
    </waypoint>
  </segment>

  <turn id='36'>
    <fromto>Pecan Row to to Guadalupe Rd.</fromto>
    <cue>LEFT onto Guadalupe Rd.</cue>
    <comments>Pecan Row dead-ends into Guadalupe Rd.</comments>
  </turn>

  <segment id='36'>
    <road>Guadalupe Rd.</road>
    <fromto>Pecan Row to River Rd.</fromto>
    <comments>Wind past houses that back-up onto the river.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='2108'>
      <lat>29.840992</lat>
      <lon>-98.172659</lon>
      <ele>230.4</ele>
      <usgs>230.728210449</usgs>
    </waypoint>
    <waypoint id='2109'>
      <lat>29.841044</lat>
      <lon>-98.172553</lon>
      <ele>230.9</ele>
      <usgs>230.546356201</usgs>
    </waypoint>
    <waypoint id='2110'>
      <lat>29.841368</lat>
      <lon>-98.172073</lon>
      <ele>230.4</ele>
      <usgs>229.39465332</usgs>
    </waypoint>
    <waypoint id='2111'>
      <lat>29.841646</lat>
      <lon>-98.171657</lon>
      <ele>230.4</ele>
      <usgs>228.272491455</usgs>
    </waypoint>
    <waypoint id='2112'>
      <lat>29.842008</lat>
      <lon>-98.171106</lon>
      <ele>231.3</ele>
      <usgs>227.511550903</usgs>
    </waypoint>
    <waypoint id='2113'>
      <lat>29.842288</lat>
      <lon>-98.170696</lon>
      <ele>230.4</ele>
      <usgs>227.182159424</usgs>
    </waypoint>
    <waypoint id='2114'>
      <lat>29.842686</lat>
      <lon>-98.170079</lon>
      <ele>229.9</ele>
      <usgs>226.143875122</usgs>
    </waypoint>
    <waypoint id='2115'>
      <lat>29.842937</lat>
      <lon>-98.169696</lon>
      <ele>229.4</ele>
      <usgs>224.82901001</usgs>
    </waypoint>
    <waypoint id='2116'>
      <lat>29.843155</lat>
      <lon>-98.169365</lon>
      <ele>229.9</ele>
      <usgs>226.126739502</usgs>
    </waypoint>
  </segment>

  <turn id='37'>
    <fromto>Guadalupe Rd. to River Rd.</fromto>
    <cue>RIGHT onto River Rd.</cue>
    <comments>Guadalupe Rd. dead-ends into River Rd.</comments>
  </turn>

  <segment id='37'>
    <road>River Rd.</road>
    <fromto>Guadalupe Rd. to River Rd.</fromto>
    <comments>When you turn right you're almost at the fourth crossing.
      Retrace your steps back down River Rd.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>30</speed>
    <waypoint id='2117'>
      <lat>29.843243</lat>
      <lon>-98.169173</lon>
      <ele>230.9</ele>
      <usgs>226.635940552</usgs>
    </waypoint>
    <waypoint id='2118'>
      <lat>29.843239</lat>
      <lon>-98.16913</lon>
      <ele>230.9</ele>
      <usgs>226.390182495</usgs>
    </waypoint>
    <waypoint id='2119'>
      <lat>29.843182</lat>
      <lon>-98.168792</lon>
      <ele>229.9</ele>
      <usgs>226.139846802</usgs>
    </waypoint>
    <waypoint id='2120'>
      <lat>29.843173</lat>
      <lon>-98.168717</lon>
      <ele>228.9</ele>
      <usgs>226.139846802</usgs>
    </waypoint>
    <waypoint id='2121'>
      <lat>29.843072</lat>
      <lon>-98.168457</lon>
      <ele>226.0</ele>
      <usgs>224.395462036</usgs>
    </waypoint>
    <waypoint id='2122'>
      <lat>29.84301</lat>
      <lon>-98.168386</lon>
      <ele>225.6</ele>
      <usgs>221.839279175</usgs>
    </waypoint>
    <waypoint id='2123'>
      <lat>29.842942</lat>
      <lon>-98.168319</lon>
      <ele>226.0</ele>
      <usgs>219.403579712</usgs>
    </waypoint>
    <waypoint id='2124' poi='5'>
      <lat>29.84266</lat>
      <lon>-98.168081</lon>
      <ele>225.1</ele>
      <usgs>219.468002319</usgs>
    </waypoint>
    <waypoint id='2125'>
      <lat>29.842406</lat>
      <lon>-98.167995</lon>
      <ele>225.6</ele>
      <usgs>226.788101196</usgs>
    </waypoint>
    <waypoint id='2126'>
      <lat>29.84227</lat>
      <lon>-98.16809</lon>
      <ele>227.5</ele>
      <usgs>227.160736084</usgs>
    </waypoint>
    <waypoint id='2127'>
      <lat>29.842061</lat>
      <lon>-98.168288</lon>
      <ele>230.9</ele>
      <usgs>227.450775146</usgs>
    </waypoint>
    <waypoint id='2128'>
      <lat>29.842008</lat>
      <lon>-98.168337</lon>
      <ele>231.3</ele>
      <usgs>227.709945679</usgs>
    </waypoint>
    <waypoint id='2129'>
      <lat>29.841778</lat>
      <lon>-98.168519</lon>
      <ele>232.8</ele>
      <usgs>228.443878174</usgs>
    </waypoint>
    <waypoint id='2130'>
      <lat>29.841506</lat>
      <lon>-98.168675</lon>
      <ele>233.3</ele>
      <usgs>230.317077637</usgs>
    </waypoint>
    <waypoint id='2131'>
      <lat>29.841212</lat>
      <lon>-98.168725</lon>
      <ele>232.8</ele>
      <usgs>232.147949219</usgs>
    </waypoint>
    <waypoint id='2132'>
      <lat>29.841127</lat>
      <lon>-98.16871</lon>
      <ele>233.3</ele>
      <usgs>232.473327637</usgs>
    </waypoint>
    <waypoint id='2133'>
      <lat>29.840809</lat>
      <lon>-98.168547</lon>
      <ele>233.7</ele>
      <usgs>233.786254883</usgs>
    </waypoint>
    <waypoint id='2134'>
      <lat>29.840503</lat>
      <lon>-98.168324</lon>
      <ele>234.2</ele>
      <usgs>235.12411499</usgs>
    </waypoint>
    <waypoint id='2135'>
      <lat>29.840129</lat>
      <lon>-98.167977</lon>
      <ele>235.2</ele>
      <usgs>236.340942383</usgs>
    </waypoint>
    <waypoint id='2136'>
      <lat>29.839803</lat>
      <lon>-98.167611</lon>
      <ele>235.7</ele>
      <usgs>238.341308594</usgs>
    </waypoint>
    <waypoint id='2137'>
      <lat>29.839553</lat>
      <lon>-98.167278</lon>
      <ele>237.6</ele>
      <usgs>242.142318726</usgs>
    </waypoint>
    <waypoint id='2138'>
      <lat>29.839301</lat>
      <lon>-98.166863</lon>
      <ele>240.5</ele>
      <usgs>244.130966187</usgs>
    </waypoint>
    <waypoint id='2139'>
      <lat>29.839076</lat>
      <lon>-98.166474</lon>
      <ele>242.4</ele>
      <usgs>246.434005737</usgs>
    </waypoint>
    <waypoint id='2140'>
      <lat>29.838852</lat>
      <lon>-98.16606</lon>
      <ele>244.8</ele>
      <usgs>246.888397217</usgs>
    </waypoint>
    <waypoint id='2141'>
      <lat>29.838578</lat>
      <lon>-98.16555</lon>
      <ele>242.9</ele>
      <usgs>246.8409729</usgs>
    </waypoint>
    <waypoint id='2142'>
      <lat>29.838374</lat>
      <lon>-98.165213</lon>
      <ele>241.9</ele>
      <usgs>246.156723022</usgs>
    </waypoint>
    <waypoint id='2143'>
      <lat>29.838124</lat>
      <lon>-98.164927</lon>
      <ele>240.5</ele>
      <usgs>245.257247925</usgs>
    </waypoint>
    <waypoint id='2144'>
      <lat>29.837744</lat>
      <lon>-98.164688</lon>
      <ele>240.5</ele>
      <usgs>239.665176392</usgs>
    </waypoint>
    <waypoint id='2145'>
      <lat>29.837456</lat>
      <lon>-98.164615</lon>
      <ele>240.5</ele>
      <usgs>238.943496704</usgs>
    </waypoint>
    <waypoint id='2146'>
      <lat>29.837056</lat>
      <lon>-98.164585</lon>
      <ele>241.4</ele>
      <usgs>241.271881104</usgs>
    </waypoint>
    <waypoint id='2147'>
      <lat>29.836724</lat>
      <lon>-98.164675</lon>
      <ele>242.4</ele>
      <usgs>242.169937134</usgs>
    </waypoint>
    <waypoint id='2148'>
      <lat>29.836184</lat>
      <lon>-98.164905</lon>
      <ele>241.4</ele>
      <usgs>242.89982605</usgs>
    </waypoint>
    <waypoint id='2149'>
      <lat>29.835734</lat>
      <lon>-98.165061</lon>
      <ele>240.9</ele>
      <usgs>242.476608276</usgs>
    </waypoint>
    <waypoint id='2150'>
      <lat>29.835422</lat>
      <lon>-98.165079</lon>
      <ele>240.9</ele>
      <usgs>242.211273193</usgs>
    </waypoint>
    <waypoint id='2151'>
      <lat>29.835051</lat>
      <lon>-98.16497</lon>
      <ele>240.0</ele>
      <usgs>241.565765381</usgs>
    </waypoint>
    <waypoint id='2152'>
      <lat>29.834723</lat>
      <lon>-98.164808</lon>
      <ele>238.5</ele>
      <usgs>241.966064453</usgs>
    </waypoint>
    <waypoint id='2153'>
      <lat>29.834246</lat>
      <lon>-98.164492</lon>
      <ele>237.6</ele>
      <usgs>240.739364624</usgs>
    </waypoint>
    <waypoint id='2154'>
      <lat>29.833847</lat>
      <lon>-98.164174</lon>
      <ele>238.1</ele>
      <usgs>241.424606323</usgs>
    </waypoint>
    <waypoint id='2155'>
      <lat>29.833368</lat>
      <lon>-98.163739</lon>
      <ele>236.6</ele>
      <usgs>242.248016357</usgs>
    </waypoint>
    <waypoint id='2156'>
      <lat>29.832857</lat>
      <lon>-98.163218</lon>
      <ele>235.2</ele>
      <usgs>238.748794556</usgs>
    </waypoint>
    <waypoint id='2157'>
      <lat>29.832432</lat>
      <lon>-98.162907</lon>
      <ele>232.8</ele>
      <usgs>237.225128174</usgs>
    </waypoint>
    <waypoint id='2158'>
      <lat>29.832283</lat>
      <lon>-98.162841</lon>
      <ele>232.3</ele>
      <usgs>236.623855591</usgs>
    </waypoint>
    <waypoint id='2159'>
      <lat>29.831879</lat>
      <lon>-98.162831</lon>
      <ele>232.3</ele>
      <usgs>234.880172729</usgs>
    </waypoint>
    <waypoint id='2160'>
      <lat>29.83166</lat>
      <lon>-98.162927</lon>
      <ele>232.3</ele>
      <usgs>233.650985718</usgs>
    </waypoint>
    <waypoint id='2161'>
      <lat>29.831188</lat>
      <lon>-98.163278</lon>
      <ele>231.8</ele>
      <usgs>232.692642212</usgs>
    </waypoint>
    <waypoint id='2162'>
      <lat>29.830495</lat>
      <lon>-98.163841</lon>
      <ele>231.3</ele>
      <usgs>232.149368286</usgs>
    </waypoint>
    <waypoint id='2163'>
      <lat>29.829909</lat>
      <lon>-98.164313</lon>
      <ele>231.8</ele>
      <usgs>232.006118774</usgs>
    </waypoint>
    <waypoint id='2164'>
      <lat>29.829342</lat>
      <lon>-98.16473</lon>
      <ele>229.4</ele>
      <usgs>229.87286377</usgs>
    </waypoint>
    <waypoint id='2165'>
      <lat>29.828953</lat>
      <lon>-98.164884</lon>
      <ele>228.9</ele>
      <usgs>228.292312622</usgs>
    </waypoint>
    <waypoint id='2166'>
      <lat>29.828492</lat>
      <lon>-98.164945</lon>
      <ele>228.9</ele>
      <usgs>228.071365356</usgs>
    </waypoint>
    <waypoint id='2167'>
      <lat>29.828368</lat>
      <lon>-98.164968</lon>
      <ele>229.9</ele>
      <usgs>228.37071228</usgs>
    </waypoint>
    <waypoint id='2168'>
      <lat>29.828123</lat>
      <lon>-98.165034</lon>
      <ele>227.5</ele>
      <usgs>228.227157593</usgs>
    </waypoint>
    <waypoint id='2169'>
      <lat>29.827716</lat>
      <lon>-98.165161</lon>
      <ele>225.1</ele>
      <usgs>225.943389893</usgs>
    </waypoint>
    <waypoint id='2170'>
      <lat>29.827481</lat>
      <lon>-98.165214</lon>
      <ele>222.7</ele>
      <usgs>220.677734375</usgs>
    </waypoint>
    <waypoint id='2171'>
      <lat>29.827145</lat>
      <lon>-98.165168</lon>
      <ele>221.2</ele>
      <usgs>220.856079102</usgs>
    </waypoint>
    <waypoint id='2172'>
      <lat>29.827056</lat>
      <lon>-98.16513</lon>
      <ele>220.3</ele>
      <usgs>221.292129517</usgs>
    </waypoint>
    <waypoint id='2173'>
      <lat>29.826872</lat>
      <lon>-98.165048</lon>
      <ele>220.3</ele>
      <usgs>223.53364563</usgs>
    </waypoint>
    <waypoint id='2174'>
      <lat>29.826551</lat>
      <lon>-98.165011</lon>
      <ele>222.2</ele>
      <usgs>225.15083313</usgs>
    </waypoint>
    <waypoint id='2175'>
      <lat>29.826272</lat>
      <lon>-98.165032</lon>
      <ele>222.7</ele>
      <usgs>225.991287231</usgs>
    </waypoint>
    <waypoint id='2176'>
      <lat>29.82595</lat>
      <lon>-98.165117</lon>
      <ele>224.1</ele>
      <usgs>226.059417725</usgs>
    </waypoint>
    <waypoint id='2177'>
      <lat>29.82546</lat>
      <lon>-98.165302</lon>
      <ele>224.1</ele>
      <usgs>226.014297485</usgs>
    </waypoint>
    <waypoint id='2178'>
      <lat>29.825004</lat>
      <lon>-98.165476</lon>
      <ele>223.6</ele>
      <usgs>225.735824585</usgs>
    </waypoint>
    <waypoint id='2179'>
      <lat>29.824472</lat>
      <lon>-98.165673</lon>
      <ele>223.6</ele>
      <usgs>225.598220825</usgs>
    </waypoint>
    <waypoint id='2180'>
      <lat>29.824033</lat>
      <lon>-98.165833</lon>
      <ele>223.6</ele>
      <usgs>226.155761719</usgs>
    </waypoint>
    <waypoint id='2181'>
      <lat>29.823493</lat>
      <lon>-98.166016</lon>
      <ele>222.7</ele>
      <usgs>226.270050049</usgs>
    </waypoint>
    <waypoint id='2182'>
      <lat>29.822943</lat>
      <lon>-98.166194</lon>
      <ele>222.7</ele>
      <usgs>226.244171143</usgs>
    </waypoint>
    <waypoint id='2183'>
      <lat>29.822553</lat>
      <lon>-98.16631</lon>
      <ele>223.2</ele>
      <usgs>226.099380493</usgs>
    </waypoint>
    <waypoint id='2184' stop='9'>
      <lat>29.822175</lat>
      <lon>-98.166422</lon>
      <ele>223.6</ele>
      <usgs>226.095474243</usgs>
    </waypoint>
    <waypoint id='2185'>
      <lat>29.821695</lat>
      <lon>-98.166566</lon>
      <ele>224.1</ele>
      <usgs>226.026931763</usgs>
    </waypoint>
    <waypoint id='2186'>
      <lat>29.821283</lat>
      <lon>-98.16669</lon>
      <ele>225.1</ele>
      <usgs>224.869369507</usgs>
    </waypoint>
    <waypoint id='2187'>
      <lat>29.820831</lat>
      <lon>-98.166855</lon>
      <ele>225.6</ele>
      <usgs>222.621948242</usgs>
    </waypoint>
    <waypoint id='2188'>
      <lat>29.820449</lat>
      <lon>-98.167089</lon>
      <ele>226.0</ele>
      <usgs>223.431915283</usgs>
    </waypoint>
    <waypoint id='2189'>
      <lat>29.820181</lat>
      <lon>-98.167364</lon>
      <ele>225.1</ele>
      <usgs>223.446655273</usgs>
    </waypoint>
    <waypoint id='2190'>
      <lat>29.819981</lat>
      <lon>-98.167632</lon>
      <ele>224.1</ele>
      <usgs>222.975967407</usgs>
    </waypoint>
    <waypoint id='2191'>
      <lat>29.819723</lat>
      <lon>-98.168067</lon>
      <ele>220.8</ele>
      <usgs>222.059356689</usgs>
    </waypoint>
    <waypoint id='2192'>
      <lat>29.819679</lat>
      <lon>-98.168168</lon>
      <ele>220.8</ele>
      <usgs>223.170150757</usgs>
    </waypoint>
    <waypoint id='2193'>
      <lat>29.819413</lat>
      <lon>-98.16891</lon>
      <ele>219.3</ele>
      <usgs>223.298919678</usgs>
    </waypoint>
    <waypoint id='2194'>
      <lat>29.819154</lat>
      <lon>-98.169671</lon>
      <ele>218.8</ele>
      <usgs>223.511611938</usgs>
    </waypoint>
    <waypoint id='2195'>
      <lat>29.818932</lat>
      <lon>-98.170356</lon>
      <ele>218.8</ele>
      <usgs>221.652603149</usgs>
    </waypoint>
    <waypoint id='2196'>
      <lat>29.818679</lat>
      <lon>-98.170937</lon>
      <ele>219.8</ele>
      <usgs>221.725479126</usgs>
    </waypoint>
    <waypoint id='2197'>
      <lat>29.81855</lat>
      <lon>-98.171211</lon>
      <ele>219.8</ele>
      <usgs>220.448745728</usgs>
    </waypoint>
    <waypoint id='2198'>
      <lat>29.818498</lat>
      <lon>-98.171372</lon>
      <ele>220.8</ele>
      <usgs>221.89805603</usgs>
    </waypoint>
    <waypoint id='2199'>
      <lat>29.818434</lat>
      <lon>-98.171651</lon>
      <ele>224.6</ele>
      <usgs>223.482284546</usgs>
    </waypoint>
    <waypoint id='2200'>
      <lat>29.818421</lat>
      <lon>-98.172054</lon>
      <ele>225.6</ele>
      <usgs>226.989685059</usgs>
    </waypoint>
    <waypoint id='2201'>
      <lat>29.81839</lat>
      <lon>-98.172412</lon>
      <ele>226.0</ele>
      <usgs>226.557800293</usgs>
    </waypoint>
    <waypoint id='2202'>
      <lat>29.818367</lat>
      <lon>-98.172521</lon>
      <ele>225.6</ele>
      <usgs>226.445053101</usgs>
    </waypoint>
    <waypoint id='2203'>
      <lat>29.818205</lat>
      <lon>-98.172775</lon>
      <ele>226.0</ele>
      <usgs>227.600708008</usgs>
    </waypoint>
    <waypoint id='2204'>
      <lat>29.818132</lat>
      <lon>-98.17283</lon>
      <ele>226.5</ele>
      <usgs>228.171127319</usgs>
    </waypoint>
    <waypoint id='2205'>
      <lat>29.817683</lat>
      <lon>-98.173072</lon>
      <ele>227.0</ele>
      <usgs>229.934371948</usgs>
    </waypoint>
    <waypoint id='2206'>
      <lat>29.817442</lat>
      <lon>-98.173231</lon>
      <ele>228.0</ele>
      <usgs>230.368087769</usgs>
    </waypoint>
    <waypoint id='2207'>
      <lat>29.817204</lat>
      <lon>-98.173388</lon>
      <ele>228.0</ele>
      <usgs>230.919784546</usgs>
    </waypoint>
    <waypoint id='2208'>
      <lat>29.816871</lat>
      <lon>-98.17372</lon>
      <ele>228.5</ele>
      <usgs>230.877243042</usgs>
    </waypoint>
    <waypoint id='2209'>
      <lat>29.816605</lat>
      <lon>-98.174024</lon>
      <ele>228.9</ele>
      <usgs>230.983383179</usgs>
    </waypoint>
    <waypoint id='2210'>
      <lat>29.816331</lat>
      <lon>-98.174299</lon>
      <ele>228.9</ele>
      <usgs>231.033432007</usgs>
    </waypoint>
    <waypoint id='2211'>
      <lat>29.815856</lat>
      <lon>-98.174699</lon>
      <ele>228.5</ele>
      <usgs>231.340744019</usgs>
    </waypoint>
    <waypoint id='2212'>
      <lat>29.815372</lat>
      <lon>-98.175035</lon>
      <ele>228.9</ele>
      <usgs>230.882003784</usgs>
    </waypoint>
    <waypoint id='2213'>
      <lat>29.815059</lat>
      <lon>-98.175244</lon>
      <ele>228.5</ele>
      <usgs>230.612533569</usgs>
    </waypoint>
    <waypoint id='2214'>
      <lat>29.814584</lat>
      <lon>-98.175502</lon>
      <ele>228.0</ele>
      <usgs>229.894439697</usgs>
    </waypoint>
    <waypoint id='2215'>
      <lat>29.814438</lat>
      <lon>-98.175556</lon>
      <ele>227.0</ele>
      <usgs>229.232330322</usgs>
    </waypoint>
    <waypoint id='2216'>
      <lat>29.814074</lat>
      <lon>-98.175633</lon>
      <ele>227.5</ele>
      <usgs>229.032150269</usgs>
    </waypoint>
    <waypoint id='2217'>
      <lat>29.813686</lat>
      <lon>-98.175552</lon>
      <ele>227.0</ele>
      <usgs>229.081771851</usgs>
    </waypoint>
    <waypoint id='2218'>
      <lat>29.813193</lat>
      <lon>-98.175255</lon>
      <ele>226.0</ele>
      <usgs>229.406112671</usgs>
    </waypoint>
    <waypoint id='2219'>
      <lat>29.81255</lat>
      <lon>-98.174849</lon>
      <ele>225.1</ele>
      <usgs>227.824111938</usgs>
    </waypoint>
    <waypoint id='2220'>
      <lat>29.812141</lat>
      <lon>-98.174603</lon>
      <ele>225.6</ele>
      <usgs>228.242874146</usgs>
    </waypoint>
    <waypoint id='2221'>
      <lat>29.811638</lat>
      <lon>-98.174296</lon>
      <ele>224.6</ele>
      <usgs>225.320724487</usgs>
    </waypoint>
    <waypoint id='2222'>
      <lat>29.811093</lat>
      <lon>-98.174036</lon>
      <ele>224.1</ele>
      <usgs>225.108963013</usgs>
    </waypoint>
    <waypoint id='2223'>
      <lat>29.810636</lat>
      <lon>-98.173891</lon>
      <ele>223.2</ele>
      <usgs>224.963500977</usgs>
    </waypoint>
    <waypoint id='2224'>
      <lat>29.809955</lat>
      <lon>-98.173699</lon>
      <ele>222.2</ele>
      <usgs>225.284835815</usgs>
    </waypoint>
    <waypoint id='2225'>
      <lat>29.809499</lat>
      <lon>-98.173581</lon>
      <ele>219.3</ele>
      <usgs>219.820236206</usgs>
    </waypoint>
    <waypoint id='2226'>
      <lat>29.809208</lat>
      <lon>-98.173482</lon>
      <ele>216.4</ele>
      <usgs>218.680664062</usgs>
    </waypoint>
    <waypoint id='2227'>
      <lat>29.809005</lat>
      <lon>-98.173382</lon>
      <ele>214.5</ele>
      <usgs>219.130767822</usgs>
    </waypoint>
    <waypoint id='2228'>
      <lat>29.808524</lat>
      <lon>-98.173014</lon>
      <ele>213.1</ele>
      <usgs>229.043746948</usgs>
    </waypoint>
    <waypoint id='2229'>
      <lat>29.808338</lat>
      <lon>-98.172908</lon>
      <ele>213.1</ele>
      <usgs>226.029220581</usgs>
    </waypoint>
    <waypoint id='2230'>
      <lat>29.807866</lat>
      <lon>-98.172822</lon>
      <ele>212.6</ele>
      <usgs>213.327270508</usgs>
    </waypoint>
    <waypoint id='2231'>
      <lat>29.807511</lat>
      <lon>-98.172872</lon>
      <ele>212.1</ele>
      <usgs>221.503448486</usgs>
    </waypoint>
    <waypoint id='2232'>
      <lat>29.807029</lat>
      <lon>-98.17304</lon>
      <ele>212.6</ele>
      <usgs>227.491439819</usgs>
    </waypoint>
    <waypoint id='2233'>
      <lat>29.80659</lat>
      <lon>-98.173153</lon>
      <ele>213.1</ele>
      <usgs>223.779846191</usgs>
    </waypoint>
    <waypoint id='2234'>
      <lat>29.80625</lat>
      <lon>-98.173212</lon>
      <ele>212.6</ele>
      <usgs>225.333068848</usgs>
    </waypoint>
    <waypoint id='2235'>
      <lat>29.80583</lat>
      <lon>-98.173283</lon>
      <ele>212.6</ele>
      <usgs>224.58366394</usgs>
    </waypoint>
    <waypoint id='2236'>
      <lat>29.805306</lat>
      <lon>-98.173343</lon>
      <ele>213.6</ele>
      <usgs>220.266067505</usgs>
    </waypoint>
    <waypoint id='2237'>
      <lat>29.804827</lat>
      <lon>-98.173301</lon>
      <ele>213.1</ele>
      <usgs>220.855392456</usgs>
    </waypoint>
    <waypoint id='2238'>
      <lat>29.80436</lat>
      <lon>-98.173225</lon>
      <ele>212.6</ele>
      <usgs>216.338378906</usgs>
    </waypoint>
    <waypoint id='2239'>
      <lat>29.803956</lat>
      <lon>-98.173113</lon>
      <ele>213.1</ele>
      <usgs>213.318878174</usgs>
    </waypoint>
    <waypoint id='2240'>
      <lat>29.80353</lat>
      <lon>-98.172933</lon>
      <ele>213.6</ele>
      <usgs>213.846710205</usgs>
    </waypoint>
    <waypoint id='2241'>
      <lat>29.803267</lat>
      <lon>-98.172779</lon>
      <ele>215.5</ele>
      <usgs>212.943664551</usgs>
    </waypoint>
    <waypoint id='2242'>
      <lat>29.80297</lat>
      <lon>-98.172557</lon>
      <ele>217.4</ele>
      <usgs>218.9947052</usgs>
    </waypoint>
    <waypoint id='2243'>
      <lat>29.802684</lat>
      <lon>-98.172321</lon>
      <ele>217.9</ele>
      <usgs>218.70022583</usgs>
    </waypoint>
    <waypoint id='2244'>
      <lat>29.802089</lat>
      <lon>-98.171854</lon>
      <ele>217.9</ele>
      <usgs>218.99458313</usgs>
    </waypoint>
    <waypoint id='2245'>
      <lat>29.801481</lat>
      <lon>-98.171357</lon>
      <ele>217.4</ele>
      <usgs>216.943710327</usgs>
    </waypoint>
    <waypoint id='2246'>
      <lat>29.801397</lat>
      <lon>-98.171255</lon>
      <ele>217.9</ele>
      <usgs>217.176864624</usgs>
    </waypoint>
    <waypoint id='2247'>
      <lat>29.801256</lat>
      <lon>-98.170883</lon>
      <ele>218.4</ele>
      <usgs>216.519989014</usgs>
    </waypoint>
    <waypoint id='2248'>
      <lat>29.801243</lat>
      <lon>-98.170748</lon>
      <ele>217.9</ele>
      <usgs>216.602035522</usgs>
    </waypoint>
    <waypoint id='2249'>
      <lat>29.801275</lat>
      <lon>-98.170147</lon>
      <ele>218.4</ele>
      <usgs>216.582077026</usgs>
    </waypoint>
    <waypoint id='2250'>
      <lat>29.80132</lat>
      <lon>-98.169512</lon>
      <ele>219.8</ele>
      <usgs>216.44380188</usgs>
    </waypoint>
    <waypoint id='2251'>
      <lat>29.801326</lat>
      <lon>-98.169436</lon>
      <ele>219.8</ele>
      <usgs>216.299118042</usgs>
    </waypoint>
    <waypoint id='2252'>
      <lat>29.801421</lat>
      <lon>-98.168796</lon>
      <ele>218.4</ele>
      <usgs>215.537490845</usgs>
    </waypoint>
    <waypoint id='2253'>
      <lat>29.801658</lat>
      <lon>-98.168066</lon>
      <ele>217.9</ele>
      <usgs>214.717407227</usgs>
    </waypoint>
    <waypoint id='2254'>
      <lat>29.801877</lat>
      <lon>-98.167637</lon>
      <ele>218.4</ele>
      <usgs>214.770523071</usgs>
    </waypoint>
    <waypoint id='2255'>
      <lat>29.8022</lat>
      <lon>-98.167138</lon>
      <ele>218.8</ele>
      <usgs>214.658248901</usgs>
    </waypoint>
    <waypoint id='2256'>
      <lat>29.802586</lat>
      <lon>-98.166538</lon>
      <ele>217.9</ele>
      <usgs>214.34828186</usgs>
    </waypoint>
    <waypoint id='2257'>
      <lat>29.802937</lat>
      <lon>-98.165969</lon>
      <ele>215.5</ele>
      <usgs>214.370025635</usgs>
    </waypoint>
    <waypoint id='2258'>
      <lat>29.803281</lat>
      <lon>-98.165401</lon>
      <ele>215.0</ele>
      <usgs>214.194030762</usgs>
    </waypoint>
    <waypoint id='2259'>
      <lat>29.803521</lat>
      <lon>-98.164925</lon>
      <ele>212.1</ele>
      <usgs>213.672332764</usgs>
    </waypoint>
    <waypoint id='2260'>
      <lat>29.803612</lat>
      <lon>-98.164709</lon>
      <ele>211.6</ele>
      <usgs>213.414993286</usgs>
    </waypoint>
    <waypoint id='2261' poi='4'>
      <lat>29.803695</lat>
      <lon>-98.164161</lon>
      <ele>211.1</ele>
      <usgs>211.518264771</usgs>
    </waypoint>
    <waypoint id='2262'>
      <lat>29.803708</lat>
      <lon>-98.163565</lon>
      <ele>211.1</ele>
      <usgs>209.261016846</usgs>
    </waypoint>
    <waypoint id='2263'>
      <lat>29.803715</lat>
      <lon>-98.163325</lon>
      <ele>211.6</ele>
      <usgs>210.456604004</usgs>
    </waypoint>
    <waypoint id='2264'>
      <lat>29.803801</lat>
      <lon>-98.163089</lon>
      <ele>212.6</ele>
      <usgs>214.79989624</usgs>
    </waypoint>
    <waypoint id='2265'>
      <lat>29.804057</lat>
      <lon>-98.162692</lon>
      <ele>214.5</ele>
      <usgs>216.219161987</usgs>
    </waypoint>
    <waypoint id='2266'>
      <lat>29.804273</lat>
      <lon>-98.162163</lon>
      <ele>216.0</ele>
      <usgs>219.001571655</usgs>
    </waypoint>
    <waypoint id='2267'>
      <lat>29.804367</lat>
      <lon>-98.161812</lon>
      <ele>217.4</ele>
      <usgs>220.454772949</usgs>
    </waypoint>
    <waypoint id='2268'>
      <lat>29.804449</lat>
      <lon>-98.161435</lon>
      <ele>219.3</ele>
      <usgs>220.924087524</usgs>
    </waypoint>
    <waypoint id='2269'>
      <lat>29.804485</lat>
      <lon>-98.161117</lon>
      <ele>219.3</ele>
      <usgs>221.249862671</usgs>
    </waypoint>
    <waypoint id='2270'>
      <lat>29.804481</lat>
      <lon>-98.160636</lon>
      <ele>220.3</ele>
      <usgs>222.518112183</usgs>
    </waypoint>
    <waypoint id='2271'>
      <lat>29.804525</lat>
      <lon>-98.1602</lon>
      <ele>220.3</ele>
      <usgs>223.077056885</usgs>
    </waypoint>
    <waypoint id='2272'>
      <lat>29.80472</lat>
      <lon>-98.159679</lon>
      <ele>218.8</ele>
      <usgs>222.351699829</usgs>
    </waypoint>
    <waypoint id='2273'>
      <lat>29.804898</lat>
      <lon>-98.159228</lon>
      <ele>218.4</ele>
      <usgs>221.434494019</usgs>
    </waypoint>
    <waypoint id='2274'>
      <lat>29.805162</lat>
      <lon>-98.158564</lon>
      <ele>216.9</ele>
      <usgs>219.876815796</usgs>
    </waypoint>
    <waypoint id='2275'>
      <lat>29.805186</lat>
      <lon>-98.158483</lon>
      <ele>217.4</ele>
      <usgs>219.170013428</usgs>
    </waypoint>
    <waypoint id='2276'>
      <lat>29.805185</lat>
      <lon>-98.158065</lon>
      <ele>216.4</ele>
      <usgs>215.708709717</usgs>
    </waypoint>
    <waypoint id='2277'>
      <lat>29.80516</lat>
      <lon>-98.157979</lon>
      <ele>216.0</ele>
      <usgs>214.80960083</usgs>
    </waypoint>
    <waypoint id='2278'>
      <lat>29.804932</lat>
      <lon>-98.157437</lon>
      <ele>217.9</ele>
      <usgs>219.669784546</usgs>
    </waypoint>
    <waypoint id='2279'>
      <lat>29.804721</lat>
      <lon>-98.157058</lon>
      <ele>220.3</ele>
      <usgs>221.38520813</usgs>
    </waypoint>
    <waypoint id='2280'>
      <lat>29.804612</lat>
      <lon>-98.156699</lon>
      <ele>220.8</ele>
      <usgs>221.89175415</usgs>
    </waypoint>
    <waypoint id='2281'>
      <lat>29.8045</lat>
      <lon>-98.156098</lon>
      <ele>220.8</ele>
      <usgs>221.481689453</usgs>
    </waypoint>
    <waypoint id='2282'>
      <lat>29.804437</lat>
      <lon>-98.15557</lon>
      <ele>219.3</ele>
      <usgs>221.824890137</usgs>
    </waypoint>
    <waypoint id='2283'>
      <lat>29.804335</lat>
      <lon>-98.154807</lon>
      <ele>220.8</ele>
      <usgs>222.134613037</usgs>
    </waypoint>
    <waypoint id='2284'>
      <lat>29.804308</lat>
      <lon>-98.154565</lon>
      <ele>218.8</ele>
      <usgs>221.908584595</usgs>
    </waypoint>
    <waypoint id='2285'>
      <lat>29.804242</lat>
      <lon>-98.15385</lon>
      <ele>217.9</ele>
      <usgs>222.574874878</usgs>
    </waypoint>
    <waypoint id='2286'>
      <lat>29.804221</lat>
      <lon>-98.15353</lon>
      <ele>217.4</ele>
      <usgs>222.388122559</usgs>
    </waypoint>
    <waypoint id='2287'>
      <lat>29.804176</lat>
      <lon>-98.15273</lon>
      <ele>217.9</ele>
      <usgs>221.718856812</usgs>
    </waypoint>
    <waypoint id='2288'>
      <lat>29.804085</lat>
      <lon>-98.152162</lon>
      <ele>216.9</ele>
      <usgs>221.821990967</usgs>
    </waypoint>
    <waypoint id='2289'>
      <lat>29.803983</lat>
      <lon>-98.151596</lon>
      <ele>216.9</ele>
      <usgs>221.325790405</usgs>
    </waypoint>
    <waypoint id='2290'>
      <lat>29.803911</lat>
      <lon>-98.151204</lon>
      <ele>216.0</ele>
      <usgs>221.308258057</usgs>
    </waypoint>
    <waypoint id='2291'>
      <lat>29.803779</lat>
      <lon>-98.150678</lon>
      <ele>215.5</ele>
      <usgs>221.488342285</usgs>
    </waypoint>
    <waypoint id='2292'>
      <lat>29.803711</lat>
      <lon>-98.150459</lon>
      <ele>214.5</ele>
      <usgs>220.394943237</usgs>
    </waypoint>
    <waypoint id='2293'>
      <lat>29.80349</lat>
      <lon>-98.149855</lon>
      <ele>215.0</ele>
      <usgs>219.180648804</usgs>
    </waypoint>
    <waypoint id='2294'>
      <lat>29.803344</lat>
      <lon>-98.149491</lon>
      <ele>214.5</ele>
      <usgs>218.248153687</usgs>
    </waypoint>
    <waypoint id='2295'>
      <lat>29.803191</lat>
      <lon>-98.149144</lon>
      <ele>214.0</ele>
      <usgs>218.206741333</usgs>
    </waypoint>
    <waypoint id='2296'>
      <lat>29.803158</lat>
      <lon>-98.149075</lon>
      <ele>215.0</ele>
      <usgs>218.206741333</usgs>
    </waypoint>
    <waypoint id='2297'>
      <lat>29.802902</lat>
      <lon>-98.148645</lon>
      <ele>214.5</ele>
      <usgs>218.084518433</usgs>
    </waypoint>
    <waypoint id='2298'>
      <lat>29.80262</lat>
      <lon>-98.148369</lon>
      <ele>216.0</ele>
      <usgs>218.108230591</usgs>
    </waypoint>
    <waypoint id='2299'>
      <lat>29.802225</lat>
      <lon>-98.148095</lon>
      <ele>215.5</ele>
      <usgs>218.192321777</usgs>
    </waypoint>
    <waypoint id='2300'>
      <lat>29.801854</lat>
      <lon>-98.147939</lon>
      <ele>215.5</ele>
      <usgs>218.251968384</usgs>
    </waypoint>
    <waypoint id='2301'>
      <lat>29.801338</lat>
      <lon>-98.147852</lon>
      <ele>217.4</ele>
      <usgs>218.375946045</usgs>
    </waypoint>
    <waypoint id='2302'>
      <lat>29.800887</lat>
      <lon>-98.147857</lon>
      <ele>216.4</ele>
      <usgs>218.395782471</usgs>
    </waypoint>
    <waypoint id='2303'>
      <lat>29.8005</lat>
      <lon>-98.14797</lon>
      <ele>216.4</ele>
      <usgs>219.056808472</usgs>
    </waypoint>
    <waypoint id='2304'>
      <lat>29.800216</lat>
      <lon>-98.148158</lon>
      <ele>217.4</ele>
      <usgs>219.463485718</usgs>
    </waypoint>
    <waypoint id='2305'>
      <lat>29.799934</lat>
      <lon>-98.14847</lon>
      <ele>216.9</ele>
      <usgs>219.26348877</usgs>
    </waypoint>
    <waypoint id='2306'>
      <lat>29.799844</lat>
      <lon>-98.148585</lon>
      <ele>216.0</ele>
      <usgs>218.647277832</usgs>
    </waypoint>
    <waypoint id='2307'>
      <lat>29.79964</lat>
      <lon>-98.148789</lon>
      <ele>216.0</ele>
      <usgs>217.981796265</usgs>
    </waypoint>
    <waypoint id='2308'>
      <lat>29.799324</lat>
      <lon>-98.148919</lon>
      <ele>215.0</ele>
      <usgs>218.057510376</usgs>
    </waypoint>
    <waypoint id='2309'>
      <lat>29.799186</lat>
      <lon>-98.148924</lon>
      <ele>214.0</ele>
      <usgs>217.771102905</usgs>
    </waypoint>
    <waypoint id='2310'>
      <lat>29.798914</lat>
      <lon>-98.148878</lon>
      <ele>213.1</ele>
      <usgs>215.853851318</usgs>
    </waypoint>
    <waypoint id='2311'>
      <lat>29.798503</lat>
      <lon>-98.148755</lon>
      <ele>213.1</ele>
      <usgs>213.484939575</usgs>
    </waypoint>
    <waypoint id='2312'>
      <lat>29.798069</lat>
      <lon>-98.148795</lon>
      <ele>212.1</ele>
      <usgs>213.617202759</usgs>
    </waypoint>
    <waypoint id='2313'>
      <lat>29.79742</lat>
      <lon>-98.14898</lon>
      <ele>210.2</ele>
      <usgs>212.093093872</usgs>
    </waypoint>
    <waypoint id='2314'>
      <lat>29.797184</lat>
      <lon>-98.149075</lon>
      <ele>208.7</ele>
      <usgs>211.425292969</usgs>
    </waypoint>
    <waypoint id='2315'>
      <lat>29.796656</lat>
      <lon>-98.149332</lon>
      <ele>207.3</ele>
      <usgs>209.703231812</usgs>
    </waypoint>
    <waypoint id='2316'>
      <lat>29.796275</lat>
      <lon>-98.149557</lon>
      <ele>208.7</ele>
      <usgs>209.43586731</usgs>
    </waypoint>
    <waypoint id='2317' stop='8'>
      <lat>29.7957</lat>
      <lon>-98.150021</lon>
      <ele>207.8</ele>
      <usgs>209.121368408</usgs>
    </waypoint>
    <waypoint id='2318'>
      <lat>29.795242</lat>
      <lon>-98.150426</lon>
      <ele>209.2</ele>
      <usgs>208.874343872</usgs>
    </waypoint>
    <waypoint id='2319'>
      <lat>29.794747</lat>
      <lon>-98.150874</lon>
      <ele>208.7</ele>
      <usgs>209.217849731</usgs>
    </waypoint>
    <waypoint id='2320'>
      <lat>29.794518</lat>
      <lon>-98.151055</lon>
      <ele>208.3</ele>
      <usgs>208.733901978</usgs>
    </waypoint>
    <waypoint id='2321'>
      <lat>29.793883</lat>
      <lon>-98.151468</lon>
      <ele>208.7</ele>
      <usgs>208.136978149</usgs>
    </waypoint>
    <waypoint id='2322'>
      <lat>29.7935</lat>
      <lon>-98.151646</lon>
      <ele>208.7</ele>
      <usgs>208.141342163</usgs>
    </waypoint>
    <waypoint id='2323'>
      <lat>29.792991</lat>
      <lon>-98.15178</lon>
      <ele>207.3</ele>
      <usgs>208.235366821</usgs>
    </waypoint>
    <waypoint id='2324'>
      <lat>29.792602</lat>
      <lon>-98.151892</lon>
      <ele>205.9</ele>
      <usgs>208.152374268</usgs>
    </waypoint>
    <waypoint id='2325'>
      <lat>29.79209</lat>
      <lon>-98.152039</lon>
      <ele>206.3</ele>
      <usgs>208.845077515</usgs>
    </waypoint>
    <waypoint id='2326'>
      <lat>29.791719</lat>
      <lon>-98.152132</lon>
      <ele>206.8</ele>
      <usgs>209.344863892</usgs>
    </waypoint>
    <waypoint id='2327'>
      <lat>29.791242</lat>
      <lon>-98.152179</lon>
      <ele>207.3</ele>
      <usgs>208.991439819</usgs>
    </waypoint>
    <waypoint id='2328'>
      <lat>29.790894</lat>
      <lon>-98.152213</lon>
      <ele>207.8</ele>
      <usgs>208.857299805</usgs>
    </waypoint>
    <waypoint id='2329'>
      <lat>29.790504</lat>
      <lon>-98.152211</lon>
      <ele>208.3</ele>
      <usgs>208.617034912</usgs>
    </waypoint>
    <waypoint id='2330'>
      <lat>29.790112</lat>
      <lon>-98.152173</lon>
      <ele>208.3</ele>
      <usgs>208.830856323</usgs>
    </waypoint>
    <waypoint id='2331'>
      <lat>29.789611</lat>
      <lon>-98.152059</lon>
      <ele>208.3</ele>
      <usgs>208.372497559</usgs>
    </waypoint>
    <waypoint id='2332'>
      <lat>29.789175</lat>
      <lon>-98.151918</lon>
      <ele>207.3</ele>
      <usgs>207.098373413</usgs>
    </waypoint>
    <waypoint id='2333'>
      <lat>29.788605</lat>
      <lon>-98.151723</lon>
      <ele>206.8</ele>
      <usgs>205.979415894</usgs>
    </waypoint>
    <waypoint id='2334'>
      <lat>29.787905</lat>
      <lon>-98.151569</lon>
      <ele>204.4</ele>
      <usgs>205.366882324</usgs>
    </waypoint>
    <waypoint id='2335'>
      <lat>29.787317</lat>
      <lon>-98.151509</lon>
      <ele>202.5</ele>
      <usgs>205.404144287</usgs>
    </waypoint>
    <waypoint id='2336'>
      <lat>29.786921</lat>
      <lon>-98.151566</lon>
      <ele>202.0</ele>
      <usgs>204.623413086</usgs>
    </waypoint>
    <waypoint id='2337'>
      <lat>29.786486</lat>
      <lon>-98.151715</lon>
      <ele>202.0</ele>
      <usgs>205.865066528</usgs>
    </waypoint>
    <waypoint id='2338'>
      <lat>29.786159</lat>
      <lon>-98.151901</lon>
      <ele>204.4</ele>
      <usgs>206.509490967</usgs>
    </waypoint>
    <waypoint id='2339'>
      <lat>29.785754</lat>
      <lon>-98.152165</lon>
      <ele>206.3</ele>
      <usgs>206.766082764</usgs>
    </waypoint>
    <waypoint id='2340'>
      <lat>29.785354</lat>
      <lon>-98.152449</lon>
      <ele>206.3</ele>
      <usgs>207.181930542</usgs>
    </waypoint>
    <waypoint id='2341'>
      <lat>29.784985</lat>
      <lon>-98.15281</lon>
      <ele>205.4</ele>
      <usgs>208.788879395</usgs>
    </waypoint>
    <waypoint id='2342'>
      <lat>29.784635</lat>
      <lon>-98.153245</lon>
      <ele>204.9</ele>
      <usgs>210.464584351</usgs>
    </waypoint>
    <waypoint id='2343'>
      <lat>29.784177</lat>
      <lon>-98.153976</lon>
      <ele>205.4</ele>
      <usgs>210.562927246</usgs>
    </waypoint>
    <waypoint id='2344'>
      <lat>29.784017</lat>
      <lon>-98.154381</lon>
      <ele>205.4</ele>
      <usgs>211.083786011</usgs>
    </waypoint>
    <waypoint id='2345'>
      <lat>29.783931</lat>
      <lon>-98.154702</lon>
      <ele>207.3</ele>
      <usgs>211.390380859</usgs>
    </waypoint>
    <waypoint id='2346'>
      <lat>29.783796</lat>
      <lon>-98.155146</lon>
      <ele>209.2</ele>
      <usgs>211.539932251</usgs>
    </waypoint>
    <waypoint id='2347'>
      <lat>29.783589</lat>
      <lon>-98.155701</lon>
      <ele>210.2</ele>
      <usgs>211.276046753</usgs>
    </waypoint>
    <waypoint id='2348'>
      <lat>29.783386</lat>
      <lon>-98.156262</lon>
      <ele>210.7</ele>
      <usgs>211.570373535</usgs>
    </waypoint>
    <waypoint id='2349'>
      <lat>29.783234</lat>
      <lon>-98.156685</lon>
      <ele>211.6</ele>
      <usgs>211.599029541</usgs>
    </waypoint>
    <waypoint id='2350'>
      <lat>29.783084</lat>
      <lon>-98.157086</lon>
      <ele>211.6</ele>
      <usgs>212.11517334</usgs>
    </waypoint>
    <waypoint id='2351'>
      <lat>29.782902</lat>
      <lon>-98.157583</lon>
      <ele>213.6</ele>
      <usgs>212.396194458</usgs>
    </waypoint>
    <waypoint id='2352'>
      <lat>29.782688</lat>
      <lon>-98.158074</lon>
      <ele>213.6</ele>
      <usgs>213.693328857</usgs>
    </waypoint>
    <waypoint id='2353'>
      <lat>29.782436</lat>
      <lon>-98.158416</lon>
      <ele>214.0</ele>
      <usgs>215.110473633</usgs>
    </waypoint>
    <waypoint id='2354'>
      <lat>29.782133</lat>
      <lon>-98.158761</lon>
      <ele>211.6</ele>
      <usgs>214.891403198</usgs>
    </waypoint>
    <waypoint id='2355'>
      <lat>29.781564</lat>
      <lon>-98.159316</lon>
      <ele>210.2</ele>
      <usgs>212.742034912</usgs>
    </waypoint>
    <waypoint id='2356'>
      <lat>29.780995</lat>
      <lon>-98.159728</lon>
      <ele>207.8</ele>
      <usgs>214.831588745</usgs>
    </waypoint>
    <waypoint id='2357'>
      <lat>29.780843</lat>
      <lon>-98.159833</lon>
      <ele>206.8</ele>
      <usgs>215.43812561</usgs>
    </waypoint>
    <waypoint id='2358'>
      <lat>29.780156</lat>
      <lon>-98.160286</lon>
      <ele>205.4</ele>
      <usgs>211.472076416</usgs>
    </waypoint>
    <waypoint id='2359'>
      <lat>29.779875</lat>
      <lon>-98.160472</lon>
      <ele>205.4</ele>
      <usgs>210.871383667</usgs>
    </waypoint>
    <waypoint id='2360'>
      <lat>29.779581</lat>
      <lon>-98.160555</lon>
      <ele>204.9</ele>
      <usgs>207.986297607</usgs>
    </waypoint>
    <waypoint id='2361'>
      <lat>29.779431</lat>
      <lon>-98.160481</lon>
      <ele>204.4</ele>
      <usgs>205.057052612</usgs>
    </waypoint>
    <waypoint id='2362'>
      <lat>29.779315</lat>
      <lon>-98.160192</lon>
      <ele>204.4</ele>
      <usgs>202.880157471</usgs>
    </waypoint>
    <waypoint id='2363'>
      <lat>29.779174</lat>
      <lon>-98.159927</lon>
      <ele>203.0</ele>
      <usgs>204.622970581</usgs>
    </waypoint>
    <waypoint id='2364' poi='3'>
      <lat>29.778956</lat>
      <lon>-98.15977</lon>
      <ele>202.5</ele>
      <usgs>206.232345581</usgs>
    </waypoint>
    <waypoint id='2365'>
      <lat>29.778787</lat>
      <lon>-98.159798</lon>
      <ele>203.0</ele>
      <usgs>206.433044434</usgs>
    </waypoint>
    <waypoint id='2366'>
      <lat>29.778626</lat>
      <lon>-98.159859</lon>
      <ele>201.5</ele>
      <usgs>205.800003052</usgs>
    </waypoint>
    <waypoint id='2367'>
      <lat>29.778044</lat>
      <lon>-98.159887</lon>
      <ele>200.6</ele>
      <usgs>206.282745361</usgs>
    </waypoint>
    <waypoint id='2368'>
      <lat>29.777586</lat>
      <lon>-98.159839</lon>
      <ele>202.0</ele>
      <usgs>205.904556274</usgs>
    </waypoint>
    <waypoint id='2369'>
      <lat>29.777223</lat>
      <lon>-98.159752</lon>
      <ele>201.5</ele>
      <usgs>206.045730591</usgs>
    </waypoint>
    <waypoint id='2370'>
      <lat>29.776769</lat>
      <lon>-98.15959</lon>
      <ele>203.0</ele>
      <usgs>205.797576904</usgs>
    </waypoint>
    <waypoint id='2371'>
      <lat>29.776255</lat>
      <lon>-98.159401</lon>
      <ele>203.0</ele>
      <usgs>203.179641724</usgs>
    </waypoint>
    <waypoint id='2372'>
      <lat>29.776193</lat>
      <lon>-98.159379</lon>
      <ele>203.0</ele>
      <usgs>202.16583252</usgs>
    </waypoint>
    <waypoint id='2373'>
      <lat>29.775593</lat>
      <lon>-98.159173</lon>
      <ele>203.5</ele>
      <usgs>208.15663147</usgs>
    </waypoint>
    <waypoint id='2374'>
      <lat>29.775015</lat>
      <lon>-98.158978</lon>
      <ele>203.9</ele>
      <usgs>210.964675903</usgs>
    </waypoint>
    <waypoint id='2375'>
      <lat>29.774533</lat>
      <lon>-98.158826</lon>
      <ele>203.0</ele>
      <usgs>209.682235718</usgs>
    </waypoint>
    <waypoint id='2376'>
      <lat>29.773857</lat>
      <lon>-98.158629</lon>
      <ele>202.5</ele>
      <usgs>205.38684082</usgs>
    </waypoint>
    <waypoint id='2377'>
      <lat>29.773316</lat>
      <lon>-98.158499</lon>
      <ele>200.6</ele>
      <usgs>201.299667358</usgs>
    </waypoint>
    <waypoint id='2378'>
      <lat>29.773157</lat>
      <lon>-98.158469</lon>
      <ele>199.1</ele>
      <usgs>201.038497925</usgs>
    </waypoint>
    <waypoint id='2379'>
      <lat>29.77252</lat>
      <lon>-98.158399</lon>
      <ele>199.6</ele>
      <usgs>201.471832275</usgs>
    </waypoint>
    <waypoint id='2380' stop='7'>
      <lat>29.77193</lat>
      <lon>-98.158341</lon>
      <ele>199.6</ele>
      <usgs>204.217651367</usgs>
    </waypoint>
    <waypoint id='2381'>
      <lat>29.771139</lat>
      <lon>-98.158319</lon>
      <ele>199.1</ele>
      <usgs>206.136291504</usgs>
    </waypoint>
    <waypoint id='2382'>
      <lat>29.77035</lat>
      <lon>-98.15835</lon>
      <ele>199.6</ele>
      <usgs>204.341781616</usgs>
    </waypoint>
    <waypoint id='2383'>
      <lat>29.769992</lat>
      <lon>-98.15838</lon>
      <ele>198.6</ele>
      <usgs>205.368209839</usgs>
    </waypoint>
    <waypoint id='2384'>
      <lat>29.76957</lat>
      <lon>-98.158392</lon>
      <ele>198.6</ele>
      <usgs>206.996398926</usgs>
    </waypoint>
    <waypoint id='2385'>
      <lat>29.76902</lat>
      <lon>-98.158439</lon>
      <ele>197.7</ele>
      <usgs>207.097366333</usgs>
    </waypoint>
    <waypoint id='2386'>
      <lat>29.768342</lat>
      <lon>-98.158526</lon>
      <ele>197.7</ele>
      <usgs>205.550918579</usgs>
    </waypoint>
    <waypoint id='2387'>
      <lat>29.767719</lat>
      <lon>-98.158578</lon>
      <ele>198.6</ele>
      <usgs>205.624633789</usgs>
    </waypoint>
    <waypoint id='2388'>
      <lat>29.767076</lat>
      <lon>-98.158558</lon>
      <ele>198.6</ele>
      <usgs>205.237792969</usgs>
    </waypoint>
    <waypoint id='2389'>
      <lat>29.766428</lat>
      <lon>-98.158482</lon>
      <ele>198.2</ele>
      <usgs>205.120315552</usgs>
    </waypoint>
    <waypoint id='2390'>
      <lat>29.765944</lat>
      <lon>-98.158326</lon>
      <ele>198.6</ele>
      <usgs>204.972076416</usgs>
    </waypoint>
    <waypoint id='2391'>
      <lat>29.765489</lat>
      <lon>-98.158071</lon>
      <ele>198.2</ele>
      <usgs>203.750793457</usgs>
    </waypoint>
    <waypoint id='2392'>
      <lat>29.765145</lat>
      <lon>-98.157761</lon>
      <ele>197.7</ele>
      <usgs>204.26550293</usgs>
    </waypoint>
    <waypoint id='2393'>
      <lat>29.764865</lat>
      <lon>-98.157388</lon>
      <ele>198.2</ele>
      <usgs>204.22644043</usgs>
    </waypoint>
    <waypoint id='2394'>
      <lat>29.764685</lat>
      <lon>-98.156974</lon>
      <ele>199.6</ele>
      <usgs>204.000442505</usgs>
    </waypoint>
    <waypoint id='2395'>
      <lat>29.764614</lat>
      <lon>-98.156576</lon>
      <ele>203.9</ele>
      <usgs>204.071929932</usgs>
    </waypoint>
    <waypoint id='2396'>
      <lat>29.764609</lat>
      <lon>-98.15651</lon>
      <ele>203.5</ele>
      <usgs>204.269378662</usgs>
    </waypoint>
    <waypoint id='2397'>
      <lat>29.764574</lat>
      <lon>-98.156109</lon>
      <ele>200.6</ele>
      <usgs>204.950714111</usgs>
    </waypoint>
    <waypoint id='2398'>
      <lat>29.764528</lat>
      <lon>-98.155506</lon>
      <ele>199.1</ele>
      <usgs>204.569534302</usgs>
    </waypoint>
    <waypoint id='2399'>
      <lat>29.764537</lat>
      <lon>-98.154872</lon>
      <ele>198.6</ele>
      <usgs>204.233520508</usgs>
    </waypoint>
    <waypoint id='2400'>
      <lat>29.764652</lat>
      <lon>-98.154303</lon>
      <ele>198.6</ele>
      <usgs>204.53565979</usgs>
    </waypoint>
    <waypoint id='2401'>
      <lat>29.764876</lat>
      <lon>-98.153585</lon>
      <ele>199.1</ele>
      <usgs>203.576202393</usgs>
    </waypoint>
    <waypoint id='2402'>
      <lat>29.76516</lat>
      <lon>-98.152717</lon>
      <ele>200.1</ele>
      <usgs>203.091934204</usgs>
    </waypoint>
    <waypoint id='2403'>
      <lat>29.765432</lat>
      <lon>-98.151931</lon>
      <ele>198.6</ele>
      <usgs>202.531524658</usgs>
    </waypoint>
    <waypoint id='2404'>
      <lat>29.765684</lat>
      <lon>-98.151241</lon>
      <ele>198.2</ele>
      <usgs>203.021057129</usgs>
    </waypoint>
    <waypoint id='2405'>
      <lat>29.765981</lat>
      <lon>-98.150401</lon>
      <ele>198.2</ele>
      <usgs>202.830490112</usgs>
    </waypoint>
    <waypoint id='2406'>
      <lat>29.766194</lat>
      <lon>-98.14978</lon>
      <ele>195.8</ele>
      <usgs>202.603179932</usgs>
    </waypoint>
    <waypoint id='2407'>
      <lat>29.766431</lat>
      <lon>-98.149074</lon>
      <ele>195.8</ele>
      <usgs>202.804397583</usgs>
    </waypoint>
    <waypoint id='2408'>
      <lat>29.766522</lat>
      <lon>-98.148818</lon>
      <ele>196.2</ele>
      <usgs>203.079696655</usgs>
    </waypoint>
    <waypoint id='2409'>
      <lat>29.766697</lat>
      <lon>-98.147929</lon>
      <ele>196.2</ele>
      <usgs>203.206176758</usgs>
    </waypoint>
    <waypoint id='2410'>
      <lat>29.766797</lat>
      <lon>-98.147189</lon>
      <ele>196.2</ele>
      <usgs>203.157653809</usgs>
    </waypoint>
    <waypoint id='2411'>
      <lat>29.766826</lat>
      <lon>-98.146264</lon>
      <ele>195.8</ele>
      <usgs>203.467300415</usgs>
    </waypoint>
    <waypoint id='2412'>
      <lat>29.766853</lat>
      <lon>-98.145453</lon>
      <ele>196.2</ele>
      <usgs>205.368057251</usgs>
    </waypoint>
    <waypoint id='2413'>
      <lat>29.766859</lat>
      <lon>-98.144877</lon>
      <ele>197.2</ele>
      <usgs>206.417663574</usgs>
    </waypoint>
    <waypoint id='2414'>
      <lat>29.766751</lat>
      <lon>-98.144415</lon>
      <ele>195.8</ele>
      <usgs>204.122406006</usgs>
    </waypoint>
    <waypoint id='2415'>
      <lat>29.766618</lat>
      <lon>-98.143932</lon>
      <ele>195.3</ele>
      <usgs>204.059875488</usgs>
    </waypoint>
    <waypoint id='2416'>
      <lat>29.766494</lat>
      <lon>-98.143546</lon>
      <ele>196.7</ele>
      <usgs>204.163986206</usgs>
    </waypoint>
    <waypoint id='2417'>
      <lat>29.76638</lat>
      <lon>-98.143149</lon>
      <ele>196.2</ele>
      <usgs>202.8515625</usgs>
    </waypoint>
    <waypoint id='2418'>
      <lat>29.766352</lat>
      <lon>-98.143071</lon>
      <ele>195.8</ele>
      <usgs>203.336746216</usgs>
    </waypoint>
    <waypoint id='2419'>
      <lat>29.766179</lat>
      <lon>-98.142534</lon>
      <ele>195.3</ele>
      <usgs>203.854812622</usgs>
    </waypoint>
    <waypoint id='2420'>
      <lat>29.766052</lat>
      <lon>-98.142171</lon>
      <ele>195.8</ele>
      <usgs>202.284805298</usgs>
    </waypoint>
    <waypoint id='2421' poi='2'>
      <lat>29.76588</lat>
      <lon>-98.141944</lon>
      <ele>196.7</ele>
      <usgs>200.46937561</usgs>
    </waypoint>
    <waypoint id='2422'>
      <lat>29.765692</lat>
      <lon>-98.14192</lon>
      <ele>196.2</ele>
      <usgs>197.557144165</usgs>
    </waypoint>
    <waypoint id='2423'>
      <lat>29.764901</lat>
      <lon>-98.14195</lon>
      <ele>195.8</ele>
      <usgs>194.979034424</usgs>
    </waypoint>
    <waypoint id='2424'>
      <lat>29.764841</lat>
      <lon>-98.141946</lon>
      <ele>195.8</ele>
      <usgs>194.979034424</usgs>
    </waypoint>
    <waypoint id='2425'>
      <lat>29.764677</lat>
      <lon>-98.141889</lon>
      <ele>196.7</ele>
      <usgs>196.556152344</usgs>
    </waypoint>
    <waypoint id='2426'>
      <lat>29.764241</lat>
      <lon>-98.141603</lon>
      <ele>197.2</ele>
      <usgs>199.427078247</usgs>
    </waypoint>
    <waypoint id='2427'>
      <lat>29.763778</lat>
      <lon>-98.141282</lon>
      <ele>197.2</ele>
      <usgs>199.706497192</usgs>
    </waypoint>
    <waypoint id='2428'>
      <lat>29.763377</lat>
      <lon>-98.141049</lon>
      <ele>197.2</ele>
      <usgs>199.877655029</usgs>
    </waypoint>
    <waypoint id='2429'>
      <lat>29.76291</lat>
      <lon>-98.140798</lon>
      <ele>197.2</ele>
      <usgs>199.488922119</usgs>
    </waypoint>
    <waypoint id='2430' stop='6'>
      <lat>29.762376</lat>
      <lon>-98.140556</lon>
      <ele>197.2</ele>
      <usgs>199.583724976</usgs>
    </waypoint>
    <waypoint id='2431'>
      <lat>29.761677</lat>
      <lon>-98.140354</lon>
      <ele>196.7</ele>
      <usgs>198.476013184</usgs>
    </waypoint>
    <waypoint id='2432'>
      <lat>29.760901</lat>
      <lon>-98.140125</lon>
      <ele>196.2</ele>
      <usgs>195.683990479</usgs>
    </waypoint>
    <waypoint id='2433'>
      <lat>29.760424</lat>
      <lon>-98.140074</lon>
      <ele>195.8</ele>
      <usgs>196.307998657</usgs>
    </waypoint>
    <waypoint id='2434'>
      <lat>29.759999</lat>
      <lon>-98.140134</lon>
      <ele>196.7</ele>
      <usgs>197.214859009</usgs>
    </waypoint>
    <waypoint id='2435'>
      <lat>29.759285</lat>
      <lon>-98.140255</lon>
      <ele>196.7</ele>
      <usgs>198.241287231</usgs>
    </waypoint>
    <waypoint id='2436'>
      <lat>29.75894</lat>
      <lon>-98.140287</lon>
      <ele>196.2</ele>
      <usgs>198.544570923</usgs>
    </waypoint>
    <waypoint id='2437'>
      <lat>29.758454</lat>
      <lon>-98.140227</lon>
      <ele>196.2</ele>
      <usgs>197.868850708</usgs>
    </waypoint>
    <waypoint id='2438'>
      <lat>29.75804</lat>
      <lon>-98.140077</lon>
      <ele>196.2</ele>
      <usgs>197.105773926</usgs>
    </waypoint>
    <waypoint id='2439'>
      <lat>29.757618</lat>
      <lon>-98.139906</lon>
      <ele>195.8</ele>
      <usgs>196.550888062</usgs>
    </waypoint>
    <waypoint id='2440'>
      <lat>29.757153</lat>
      <lon>-98.13969</lon>
      <ele>195.8</ele>
      <usgs>195.916320801</usgs>
    </waypoint>
    <waypoint id='2441'>
      <lat>29.756917</lat>
      <lon>-98.139569</lon>
      <ele>193.8</ele>
      <usgs>195.63961792</usgs>
    </waypoint>
    <waypoint id='2442'>
      <lat>29.756492</lat>
      <lon>-98.139374</lon>
      <ele>193.4</ele>
      <usgs>195.360580444</usgs>
    </waypoint>
    <waypoint id='2443'>
      <lat>29.756159</lat>
      <lon>-98.139423</lon>
      <ele>192.9</ele>
      <usgs>195.186660767</usgs>
    </waypoint>
    <waypoint id='2444'>
      <lat>29.755988</lat>
      <lon>-98.139627</lon>
      <ele>192.9</ele>
      <usgs>194.085632324</usgs>
    </waypoint>
    <waypoint id='2445'>
      <lat>29.755936</lat>
      <lon>-98.139803</lon>
      <ele>193.8</ele>
      <usgs>195.575775146</usgs>
    </waypoint>
    <waypoint id='2446'>
      <lat>29.755865</lat>
      <lon>-98.140267</lon>
      <ele>195.8</ele>
      <usgs>199.640426636</usgs>
    </waypoint>
    <waypoint id='2447'>
      <lat>29.755789</lat>
      <lon>-98.140613</lon>
      <ele>197.7</ele>
      <usgs>202.603118896</usgs>
    </waypoint>
    <waypoint id='2448'>
      <lat>29.755652</lat>
      <lon>-98.140902</lon>
      <ele>199.1</ele>
      <usgs>204.764068604</usgs>
    </waypoint>
    <waypoint id='2449'>
      <lat>29.7554</lat>
      <lon>-98.141187</lon>
      <ele>202.0</ele>
      <usgs>206.551010132</usgs>
    </waypoint>
    <waypoint id='2450'>
      <lat>29.755361</lat>
      <lon>-98.141226</lon>
      <ele>202.0</ele>
      <usgs>206.979888916</usgs>
    </waypoint>
    <waypoint id='2451'>
      <lat>29.754924</lat>
      <lon>-98.141655</lon>
      <ele>202.5</ele>
      <usgs>208.855010986</usgs>
    </waypoint>
    <waypoint id='2452'>
      <lat>29.754511</lat>
      <lon>-98.142063</lon>
      <ele>203.9</ele>
      <usgs>211.333145142</usgs>
    </waypoint>
    <waypoint id='2453'>
      <lat>29.754123</lat>
      <lon>-98.142495</lon>
      <ele>206.8</ele>
      <usgs>212.943237305</usgs>
    </waypoint>
    <waypoint id='2454'>
      <lat>29.753882</lat>
      <lon>-98.142821</lon>
      <ele>208.7</ele>
      <usgs>213.692001343</usgs>
    </waypoint>
    <waypoint id='2455'>
      <lat>29.753797</lat>
      <lon>-98.142939</lon>
      <ele>210.7</ele>
      <usgs>213.525421143</usgs>
    </waypoint>
    <waypoint id='2456'>
      <lat>29.753525</lat>
      <lon>-98.143299</lon>
      <ele>213.6</ele>
      <usgs>214.706268311</usgs>
    </waypoint>
    <waypoint id='2457'>
      <lat>29.753396</lat>
      <lon>-98.143465</lon>
      <ele>215.0</ele>
      <usgs>218.673965454</usgs>
    </waypoint>
    <waypoint id='2458'>
      <lat>29.753275</lat>
      <lon>-98.14359</lon>
      <ele>216.9</ele>
      <usgs>219.383346558</usgs>
    </waypoint>
    <waypoint id='2459'>
      <lat>29.753024</lat>
      <lon>-98.143764</lon>
      <ele>218.4</ele>
      <usgs>220.037780762</usgs>
    </waypoint>
    <waypoint id='2460'>
      <lat>29.752699</lat>
      <lon>-98.143963</lon>
      <ele>220.8</ele>
      <usgs>221.693893433</usgs>
    </waypoint>
    <waypoint id='2461'>
      <lat>29.752366</lat>
      <lon>-98.144162</lon>
      <ele>222.2</ele>
      <usgs>223.738327026</usgs>
    </waypoint>
    <waypoint id='2462'>
      <lat>29.751962</lat>
      <lon>-98.144393</lon>
      <ele>222.2</ele>
      <usgs>224.444793701</usgs>
    </waypoint>
    <waypoint id='2463'>
      <lat>29.75164</lat>
      <lon>-98.144495</lon>
      <ele>222.2</ele>
      <usgs>224.573608398</usgs>
    </waypoint>
    <waypoint id='2464'>
      <lat>29.751192</lat>
      <lon>-98.144561</lon>
      <ele>223.2</ele>
      <usgs>225.293228149</usgs>
    </waypoint>
    <waypoint id='2465'>
      <lat>29.750759</lat>
      <lon>-98.144522</lon>
      <ele>223.6</ele>
      <usgs>224.103469849</usgs>
    </waypoint>
    <waypoint id='2466'>
      <lat>29.750345</lat>
      <lon>-98.144456</lon>
      <ele>223.2</ele>
      <usgs>223.535476685</usgs>
    </waypoint>
    <waypoint id='2467'>
      <lat>29.750032</lat>
      <lon>-98.144411</lon>
      <ele>224.1</ele>
      <usgs>225.987594604</usgs>
    </waypoint>
    <waypoint id='2468'>
      <lat>29.749598</lat>
      <lon>-98.14435</lon>
      <ele>225.6</ele>
      <usgs>229.262954712</usgs>
    </waypoint>
    <waypoint id='2469'>
      <lat>29.749225</lat>
      <lon>-98.144296</lon>
      <ele>227.5</ele>
      <usgs>230.444564819</usgs>
    </waypoint>
    <waypoint id='2470'>
      <lat>29.748823</lat>
      <lon>-98.144283</lon>
      <ele>228.9</ele>
      <usgs>231.303421021</usgs>
    </waypoint>
    <waypoint id='2471'>
      <lat>29.748416</lat>
      <lon>-98.144416</lon>
      <ele>229.4</ele>
      <usgs>233.521209717</usgs>
    </waypoint>
    <waypoint id='2472'>
      <lat>29.747977</lat>
      <lon>-98.144657</lon>
      <ele>231.3</ele>
      <usgs>236.03604126</usgs>
    </waypoint>
    <waypoint id='2473'>
      <lat>29.747647</lat>
      <lon>-98.1449</lon>
      <ele>230.9</ele>
      <usgs>236.204818726</usgs>
    </waypoint>
    <waypoint id='2474'>
      <lat>29.747514</lat>
      <lon>-98.145014</lon>
      <ele>230.4</ele>
      <usgs>236.539764404</usgs>
    </waypoint>
    <waypoint id='2478'>
      <lat>29.747377</lat>
      <lon>-98.145129</lon>
      <ele>230.9</ele>
      <usgs>235.94519043</usgs>
    </waypoint>
    <waypoint id='2479' stop='5'>
      <lat>29.747267</lat>
      <lon>-98.145209</lon>
      <ele>230.9</ele>
      <usgs>235.798553467</usgs>
    </waypoint>
    <waypoint id='2480'>
      <lat>29.747118</lat>
      <lon>-98.145315</lon>
      <ele>230.4</ele>
      <usgs>235.311141968</usgs>
    </waypoint>
  </segment>

  <turn id='38'>
    <fromto>River Rd. to River Rd.</fromto>
    <cue>LEFT onto River Rd.</cue>
    <comments>Turn left at the 'Y'.  The River Rd. Icehouse is on the
      corner.</comments>
  </turn>

  <segment id='38'>
    <road>River Rd.</road>
    <fromto>River Rd. to River Rd.</fromto>
    <comments>Wind past fields and a few houses.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>40</speed>
    <waypoint id='2481'>
      <lat>29.747103</lat>
      <lon>-98.145321</lon>
      <ele>230.9</ele>
      <usgs>235.311141968</usgs>
    </waypoint>
    <waypoint id='2482'>
      <lat>29.746974</lat>
      <lon>-98.145292</lon>
      <ele>230.9</ele>
      <usgs>234.959213257</usgs>
    </waypoint>
    <waypoint id='2483'>
      <lat>29.7467</lat>
      <lon>-98.145086</lon>
      <ele>230.9</ele>
      <usgs>234.229064941</usgs>
    </waypoint>
    <waypoint id='2484'>
      <lat>29.746354</lat>
      <lon>-98.144745</lon>
      <ele>233.7</ele>
      <usgs>235.145050049</usgs>
    </waypoint>
    <waypoint id='2485'>
      <lat>29.746171</lat>
      <lon>-98.144412</lon>
      <ele>233.3</ele>
      <usgs>236.404708862</usgs>
    </waypoint>
    <waypoint id='2486'>
      <lat>29.746001</lat>
      <lon>-98.14391</lon>
      <ele>233.7</ele>
      <usgs>237.158187866</usgs>
    </waypoint>
    <waypoint id='2487'>
      <lat>29.745816</lat>
      <lon>-98.143373</lon>
      <ele>233.7</ele>
      <usgs>237.117111206</usgs>
    </waypoint>
    <waypoint id='2488'>
      <lat>29.745624</lat>
      <lon>-98.142774</lon>
      <ele>232.8</ele>
      <usgs>234.617919922</usgs>
    </waypoint>
    <waypoint id='2489'>
      <lat>29.745482</lat>
      <lon>-98.142339</lon>
      <ele>229.4</ele>
      <usgs>233.240600586</usgs>
    </waypoint>
    <waypoint id='2490'>
      <lat>29.745452</lat>
      <lon>-98.142249</lon>
      <ele>229.9</ele>
      <usgs>232.213943481</usgs>
    </waypoint>
    <waypoint id='2491'>
      <lat>29.745119</lat>
      <lon>-98.141275</lon>
      <ele>228.5</ele>
      <usgs>231.418762207</usgs>
    </waypoint>
    <waypoint id='2492'>
      <lat>29.744865</lat>
      <lon>-98.140675</lon>
      <ele>228.9</ele>
      <usgs>232.679016113</usgs>
    </waypoint>
    <waypoint id='2493'>
      <lat>29.744517</lat>
      <lon>-98.139993</lon>
      <ele>228.5</ele>
      <usgs>231.464477539</usgs>
    </waypoint>
    <waypoint id='2494'>
      <lat>29.744392</lat>
      <lon>-98.139756</lon>
      <ele>227.0</ele>
      <usgs>230.298202515</usgs>
    </waypoint>
    <waypoint id='2495'>
      <lat>29.744123</lat>
      <lon>-98.139251</lon>
      <ele>224.6</ele>
      <usgs>228.722640991</usgs>
    </waypoint>
    <waypoint id='2496'>
      <lat>29.743476</lat>
      <lon>-98.138021</lon>
      <ele>222.2</ele>
      <usgs>224.6900177</usgs>
    </waypoint>
    <waypoint id='2497'>
      <lat>29.742974</lat>
      <lon>-98.137065</lon>
      <ele>221.7</ele>
      <usgs>223.97593689</usgs>
    </waypoint>
    <waypoint id='2498'>
      <lat>29.742603</lat>
      <lon>-98.136364</lon>
      <ele>222.2</ele>
      <usgs>226.110214233</usgs>
    </waypoint>
    <waypoint id='2499'>
      <lat>29.742161</lat>
      <lon>-98.135522</lon>
      <ele>222.7</ele>
      <usgs>228.017837524</usgs>
    </waypoint>
    <waypoint id='2500'>
      <lat>29.741794</lat>
      <lon>-98.134817</lon>
      <ele>223.6</ele>
      <usgs>229.327850342</usgs>
    </waypoint>
    <waypoint id='2501'>
      <lat>29.741346</lat>
      <lon>-98.133959</lon>
      <ele>225.1</ele>
      <usgs>231.35256958</usgs>
    </waypoint>
    <waypoint id='2502'>
      <lat>29.741029</lat>
      <lon>-98.133353</lon>
      <ele>223.6</ele>
      <usgs>229.187942505</usgs>
    </waypoint>
    <waypoint id='2503'>
      <lat>29.740947</lat>
      <lon>-98.133206</lon>
      <ele>222.7</ele>
      <usgs>228.736236572</usgs>
    </waypoint>
    <waypoint id='2504'>
      <lat>29.740566</lat>
      <lon>-98.132602</lon>
      <ele>221.7</ele>
      <usgs>226.163116455</usgs>
    </waypoint>
    <waypoint id='2505'>
      <lat>29.740251</lat>
      <lon>-98.132228</lon>
      <ele>221.7</ele>
      <usgs>226.349456787</usgs>
    </waypoint>
    <waypoint id='2506'>
      <lat>29.739839</lat>
      <lon>-98.131856</lon>
      <ele>222.7</ele>
      <usgs>227.155563354</usgs>
    </waypoint>
    <waypoint id='2507'>
      <lat>29.739386</lat>
      <lon>-98.131534</lon>
      <ele>223.2</ele>
      <usgs>228.900543213</usgs>
    </waypoint>
    <waypoint id='2508'>
      <lat>29.738933</lat>
      <lon>-98.131295</lon>
      <ele>224.6</ele>
      <usgs>230.147857666</usgs>
    </waypoint>
    <waypoint id='2509'>
      <lat>29.738414</lat>
      <lon>-98.131043</lon>
      <ele>224.6</ele>
      <usgs>231.254898071</usgs>
    </waypoint>
    <waypoint id='2510'>
      <lat>29.737926</lat>
      <lon>-98.130803</lon>
      <ele>224.1</ele>
      <usgs>229.239593506</usgs>
    </waypoint>
    <waypoint id='2511'>
      <lat>29.737329</lat>
      <lon>-98.130519</lon>
      <ele>223.6</ele>
      <usgs>228.496246338</usgs>
    </waypoint>
    <waypoint id='2512'>
      <lat>29.736827</lat>
      <lon>-98.130274</lon>
      <ele>221.7</ele>
      <usgs>225.794662476</usgs>
    </waypoint>
    <waypoint id='2513'>
      <lat>29.736334</lat>
      <lon>-98.130016</lon>
      <ele>218.8</ele>
      <usgs>223.079284668</usgs>
    </waypoint>
    <waypoint id='2514'>
      <lat>29.73625</lat>
      <lon>-98.129968</lon>
      <ele>219.3</ele>
      <usgs>222.898117065</usgs>
    </waypoint>
    <waypoint id='2515'>
      <lat>29.735913</lat>
      <lon>-98.129761</lon>
      <ele>217.4</ele>
      <usgs>220.614898682</usgs>
    </waypoint>
    <waypoint id='2516'>
      <lat>29.735294</lat>
      <lon>-98.129322</lon>
      <ele>215.5</ele>
      <usgs>217.515319824</usgs>
    </waypoint>
    <waypoint id='2517'>
      <lat>29.734852</lat>
      <lon>-98.128982</lon>
      <ele>213.6</ele>
      <usgs>215.354019165</usgs>
    </waypoint>
    <waypoint id='2518'>
      <lat>29.734304</lat>
      <lon>-98.128552</lon>
      <ele>209.7</ele>
      <usgs>211.603713989</usgs>
    </waypoint>
    <waypoint id='2519'>
      <lat>29.733888</lat>
      <lon>-98.128219</lon>
      <ele>205.9</ele>
      <usgs>205.289505005</usgs>
    </waypoint>
    <waypoint id='2520'>
      <lat>29.733777</lat>
      <lon>-98.128132</lon>
      <ele>205.9</ele>
      <usgs>204.413040161</usgs>
    </waypoint>
    <waypoint id='2521'>
      <lat>29.733225</lat>
      <lon>-98.127697</lon>
      <ele>203.0</ele>
      <usgs>201.764678955</usgs>
    </waypoint>
    <waypoint id='2522'>
      <lat>29.732483</lat>
      <lon>-98.127116</lon>
      <ele>200.1</ele>
      <usgs>198.840911865</usgs>
    </waypoint>
    <waypoint id='2523'>
      <lat>29.732032</lat>
      <lon>-98.126757</lon>
      <ele>201.1</ele>
      <usgs>202.567398071</usgs>
    </waypoint>
    <waypoint id='2524'>
      <lat>29.731646</lat>
      <lon>-98.126453</lon>
      <ele>204.4</ele>
      <usgs>203.811264038</usgs>
    </waypoint>
    <waypoint id='2525'>
      <lat>29.731129</lat>
      <lon>-98.126068</lon>
      <ele>204.4</ele>
      <usgs>206.035705566</usgs>
    </waypoint>
    <waypoint id='2526'>
      <lat>29.73064</lat>
      <lon>-98.125765</lon>
      <ele>204.9</ele>
      <usgs>205.442947388</usgs>
    </waypoint>
    <waypoint id='2527'>
      <lat>29.730351</lat>
      <lon>-98.125658</lon>
      <ele>204.9</ele>
      <usgs>205.258728027</usgs>
    </waypoint>
    <waypoint id='2528'>
      <lat>29.729874</lat>
      <lon>-98.125566</lon>
      <ele>203.9</ele>
      <usgs>205.402572632</usgs>
    </waypoint>
    <waypoint id='2529'>
      <lat>29.729814</lat>
      <lon>-98.125559</lon>
      <ele>203.5</ele>
      <usgs>205.702957153</usgs>
    </waypoint>
    <waypoint id='2530' stop='3'>
      <lat>29.729472</lat>
      <lon>-98.125519</lon>
      <ele>202.5</ele>
      <usgs>205.879440308</usgs>
    </waypoint>
  </segment>

  <turn id='39'>
    <fromto>River Rd. to River Rd.</fromto>
    <cue>STRAIGHT on River Rd. (through the light)</cue>
    <comments>When you cross Loop 337, River Rd. becomes calm and
      peaceful.</comments>
  </turn>

  <segment id='39'>
    <road>River Rd.</road>
    <fromto>River Rd. to Lakeview Blvd.</fromto>
    <comments>Go past some industrial stuff on the right and fields on the
      left.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='2531'>
      <lat>29.729131</lat>
      <lon>-98.125483</lon>
      <ele>202.5</ele>
      <usgs>204.410263062</usgs>
    </waypoint>
    <waypoint id='2532'>
      <lat>29.72879</lat>
      <lon>-98.125437</lon>
      <ele>202.0</ele>
      <usgs>203.153823853</usgs>
    </waypoint>
    <waypoint id='2533'>
      <lat>29.728678</lat>
      <lon>-98.125417</lon>
      <ele>201.1</ele>
      <usgs>202.82975769</usgs>
    </waypoint>
    <waypoint id='2534'>
      <lat>29.728475</lat>
      <lon>-98.125361</lon>
      <ele>199.1</ele>
      <usgs>201.782241821</usgs>
    </waypoint>
    <waypoint id='2535'>
      <lat>29.728294</lat>
      <lon>-98.125287</lon>
      <ele>196.7</ele>
      <usgs>201.136322021</usgs>
    </waypoint>
    <waypoint id='2536'>
      <lat>29.72827</lat>
      <lon>-98.125266</lon>
      <ele>196.2</ele>
      <usgs>200.717300415</usgs>
    </waypoint>
    <waypoint id='2537'>
      <lat>29.72827</lat>
      <lon>-98.125244</lon>
      <ele>197.2</ele>
      <usgs>200.717300415</usgs>
    </waypoint>
    <waypoint id='2538'>
      <lat>29.728157</lat>
      <lon>-98.125256</lon>
      <ele>197.7</ele>
      <usgs>200.331314087</usgs>
    </waypoint>
    <waypoint id='2539'>
      <lat>29.72812</lat>
      <lon>-98.125248</lon>
      <ele>197.7</ele>
      <usgs>199.821685791</usgs>
    </waypoint>
    <waypoint id='2540'>
      <lat>29.727749</lat>
      <lon>-98.125188</lon>
      <ele>195.3</ele>
      <usgs>198.258361816</usgs>
    </waypoint>
    <waypoint id='2541'>
      <lat>29.727578</lat>
      <lon>-98.125162</lon>
      <ele>193.8</ele>
      <usgs>197.64364624</usgs>
    </waypoint>
    <waypoint id='2542'>
      <lat>29.727163</lat>
      <lon>-98.125094</lon>
      <ele>193.4</ele>
      <usgs>196.63168335</usgs>
    </waypoint>
    <waypoint id='2543'>
      <lat>29.726712</lat>
      <lon>-98.124937</lon>
      <ele>193.8</ele>
      <usgs>195.222381592</usgs>
    </waypoint>
    <waypoint id='2544'>
      <lat>29.726347</lat>
      <lon>-98.12467</lon>
      <ele>192.4</ele>
      <usgs>194.544311523</usgs>
    </waypoint>
    <waypoint id='2545'>
      <lat>29.725949</lat>
      <lon>-98.124364</lon>
      <ele>191.9</ele>
      <usgs>193.891967773</usgs>
    </waypoint>
    <waypoint id='2546'>
      <lat>29.725481</lat>
      <lon>-98.124156</lon>
      <ele>190.5</ele>
      <usgs>193.989318848</usgs>
    </waypoint>
    <waypoint id='2547'>
      <lat>29.725087</lat>
      <lon>-98.124</lon>
      <ele>191.9</ele>
      <usgs>194.138946533</usgs>
    </waypoint>
    <waypoint id='2548'>
      <lat>29.724648</lat>
      <lon>-98.123862</lon>
      <ele>191.4</ele>
      <usgs>194.128723145</usgs>
    </waypoint>
    <waypoint id='2549'>
      <lat>29.724069</lat>
      <lon>-98.123715</lon>
      <ele>191.4</ele>
      <usgs>192.731124878</usgs>
    </waypoint>
    <waypoint id='2550'>
      <lat>29.723749</lat>
      <lon>-98.123636</lon>
      <ele>190.0</ele>
      <usgs>192.513717651</usgs>
    </waypoint>
    <waypoint id='2551'>
      <lat>29.723248</lat>
      <lon>-98.123539</lon>
      <ele>190.0</ele>
      <usgs>192.485107422</usgs>
    </waypoint>
    <waypoint id='2552'>
      <lat>29.722832</lat>
      <lon>-98.123544</lon>
      <ele>190.0</ele>
      <usgs>192.393081665</usgs>
    </waypoint>
    <waypoint id='2553'>
      <lat>29.722437</lat>
      <lon>-98.123544</lon>
      <ele>189.5</ele>
      <usgs>192.318557739</usgs>
    </waypoint>
    <waypoint id='2554'>
      <lat>29.722138</lat>
      <lon>-98.123444</lon>
      <ele>188.6</ele>
      <usgs>192.285140991</usgs>
    </waypoint>
    <waypoint id='2555'>
      <lat>29.722023</lat>
      <lon>-98.123384</lon>
      <ele>188.6</ele>
      <usgs>192.259368896</usgs>
    </waypoint>
    <waypoint id='2556'>
      <lat>29.7218</lat>
      <lon>-98.123441</lon>
      <ele>189.0</ele>
      <usgs>192.130279541</usgs>
    </waypoint>
    <waypoint id='2557'>
      <lat>29.721649</lat>
      <lon>-98.123608</lon>
      <ele>190.5</ele>
      <usgs>192.165710449</usgs>
    </waypoint>
    <waypoint id='2558'>
      <lat>29.721579</lat>
      <lon>-98.123679</lon>
      <ele>190.5</ele>
      <usgs>192.206634521</usgs>
    </waypoint>
  </segment>

  <turn id='40'>
    <fromto>River Rd. to Lakeview Blvd.</fromto>
    <cue>LEFT onto Lakeview Blvd.</cue>
    <comments></comments>
  </turn>

  <segment id='40'>
    <road>Lakeview Blvd.</road>
    <fromto>River Rd. to Torrey St.</fromto>
    <comments>Residential street.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='2559'>
      <lat>29.721417</lat>
      <lon>-98.123712</lon>
      <ele>190.5</ele>
      <usgs>192.251144409</usgs>
    </waypoint>
    <waypoint id='2560'>
      <lat>29.721334</lat>
      <lon>-98.123654</lon>
      <ele>190.0</ele>
      <usgs>192.225799561</usgs>
    </waypoint>
    <waypoint id='2561'>
      <lat>29.72121</lat>
      <lon>-98.123531</lon>
      <ele>189.0</ele>
      <usgs>192.214294434</usgs>
    </waypoint>
    <waypoint id='2562'>
      <lat>29.720935</lat>
      <lon>-98.123217</lon>
      <ele>188.6</ele>
      <usgs>192.128967285</usgs>
    </waypoint>
    <waypoint id='2563'>
      <lat>29.720675</lat>
      <lon>-98.122968</lon>
      <ele>190.5</ele>
      <usgs>195.410629272</usgs>
    </waypoint>
    <waypoint id='2564'>
      <lat>29.720445</lat>
      <lon>-98.122733</lon>
      <ele>194.8</ele>
      <usgs>195.97857666</usgs>
    </waypoint>
    <waypoint id='2565'>
      <lat>29.720419</lat>
      <lon>-98.122702</lon>
      <ele>194.8</ele>
      <usgs>195.97857666</usgs>
    </waypoint>
    <waypoint id='2566'>
      <lat>29.72021</lat>
      <lon>-98.122447</lon>
      <ele>193.4</ele>
      <usgs>196.169281006</usgs>
    </waypoint>
    <waypoint id='2567'>
      <lat>29.719999</lat>
      <lon>-98.122193</lon>
      <ele>192.9</ele>
      <usgs>196.150024414</usgs>
    </waypoint>
    <waypoint id='2568'>
      <lat>29.719818</lat>
      <lon>-98.12196</lon>
      <ele>192.4</ele>
      <usgs>196.040145874</usgs>
    </waypoint>
  </segment>

  <turn id='41'>
    <fromto>Lakeview Blvd. to Torrey St.</fromto>
    <cue>LEFT onto Torrey St.</cue>
    <comments></comments>
  </turn>

  <segment id='41'>
    <road>Torrey St.</road>
    <fromto>Lakeview Blvd. to Gruene Rd.</fromto>
    <comments>Residential street</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='2569'>
      <lat>29.719756</lat>
      <lon>-98.121876</lon>
      <ele>192.4</ele>
      <usgs>195.958282471</usgs>
    </waypoint>
    <waypoint id='2570'>
      <lat>29.719812</lat>
      <lon>-98.12171</lon>
      <ele>192.4</ele>
      <usgs>195.67175293</usgs>
    </waypoint>
    <waypoint id='2571'>
      <lat>29.719882</lat>
      <lon>-98.12163</lon>
      <ele>191.9</ele>
      <usgs>195.450576782</usgs>
    </waypoint>
    <waypoint id='2572'>
      <lat>29.720173</lat>
      <lon>-98.121319</lon>
      <ele>191.4</ele>
      <usgs>194.657699585</usgs>
    </waypoint>
    <waypoint id='2573'>
      <lat>29.720462</lat>
      <lon>-98.121008</lon>
      <ele>191.0</ele>
      <usgs>193.149871826</usgs>
    </waypoint>
    <waypoint id='2574'>
      <lat>29.720862</lat>
      <lon>-98.120581</lon>
      <ele>190.0</ele>
      <usgs>192.236572266</usgs>
    </waypoint>
    <waypoint id='2575'>
      <lat>29.721298</lat>
      <lon>-98.12013</lon>
      <ele>190.0</ele>
      <usgs>193.051300049</usgs>
    </waypoint>
    <waypoint id='2576'>
      <lat>29.721704</lat>
      <lon>-98.119686</lon>
      <ele>189.5</ele>
      <usgs>194.352416992</usgs>
    </waypoint>
    <waypoint id='2577'>
      <lat>29.722167</lat>
      <lon>-98.119184</lon>
      <ele>189.5</ele>
      <usgs>193.339141846</usgs>
    </waypoint>
    <waypoint id='2578'>
      <lat>29.722609</lat>
      <lon>-98.118706</lon>
      <ele>189.5</ele>
      <usgs>190.650939941</usgs>
    </waypoint>
    <waypoint id='2579'>
      <lat>29.723095</lat>
      <lon>-98.118184</lon>
      <ele>189.0</ele>
      <usgs>190.061660767</usgs>
    </waypoint>
    <waypoint id='2580'>
      <lat>29.723545</lat>
      <lon>-98.117698</lon>
      <ele>188.6</ele>
      <usgs>189.889312744</usgs>
    </waypoint>
    <waypoint id='2581'>
      <lat>29.723739</lat>
      <lon>-98.117494</lon>
      <ele>188.1</ele>
      <usgs>190.145874023</usgs>
    </waypoint>
  </segment>

  <turn id='42'>
    <fromto>Torrey St. to Gruene Rd.</fromto>
    <cue>LEFT onto Gruene Rd.</cue>
    <comments></comments>
  </turn>

  <segment id='42'>
    <road>Gruene Rd.</road>
    <fromto>Torrey St. to parking lot</fromto>
    <comments>Ride along the railroad tracks, under 46, the back down to the
      river before heading up the big hill into Gruene.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='2582'>
      <lat>29.723772</lat>
      <lon>-98.117469</lon>
      <ele>188.6</ele>
      <usgs>190.145874023</usgs>
    </waypoint>
    <waypoint id='2583'>
      <lat>29.723923</lat>
      <lon>-98.117539</lon>
      <ele>188.6</ele>
      <usgs>190.604888916</usgs>
    </waypoint>
    <waypoint id='2584'>
      <lat>29.724275</lat>
      <lon>-98.117924</lon>
      <ele>188.6</ele>
      <usgs>191.485321045</usgs>
    </waypoint>
    <waypoint id='2585'>
      <lat>29.724523</lat>
      <lon>-98.118222</lon>
      <ele>189.0</ele>
      <usgs>191.836532593</usgs>
    </waypoint>
    <waypoint id='2586'>
      <lat>29.724729</lat>
      <lon>-98.118457</lon>
      <ele>189.5</ele>
      <usgs>193.059020996</usgs>
    </waypoint>
    <waypoint id='2587'>
      <lat>29.725042</lat>
      <lon>-98.118793</lon>
      <ele>191.4</ele>
      <usgs>194.600387573</usgs>
    </waypoint>
    <waypoint id='2588'>
      <lat>29.725388</lat>
      <lon>-98.119154</lon>
      <ele>194.3</ele>
      <usgs>196.299682617</usgs>
    </waypoint>
    <waypoint id='2589'>
      <lat>29.725606</lat>
      <lon>-98.119204</lon>
      <ele>194.8</ele>
      <usgs>197.089096069</usgs>
    </waypoint>
    <waypoint id='2590'>
      <lat>29.725693</lat>
      <lon>-98.119166</lon>
      <ele>195.8</ele>
      <usgs>197.418807983</usgs>
    </waypoint>
    <waypoint id='2591'>
      <lat>29.726167</lat>
      <lon>-98.118886</lon>
      <ele>196.2</ele>
      <usgs>197.847259521</usgs>
    </waypoint>
    <waypoint id='2592'>
      <lat>29.726763</lat>
      <lon>-98.118529</lon>
      <ele>196.2</ele>
      <usgs>198.095397949</usgs>
    </waypoint>
    <waypoint id='2593'>
      <lat>29.727313</lat>
      <lon>-98.118195</lon>
      <ele>196.7</ele>
      <usgs>197.413848877</usgs>
    </waypoint>
    <waypoint id='2594'>
      <lat>29.727886</lat>
      <lon>-98.117842</lon>
      <ele>197.7</ele>
      <usgs>197.310714722</usgs>
    </waypoint>
    <waypoint id='2595'>
      <lat>29.728419</lat>
      <lon>-98.11753</lon>
      <ele>196.7</ele>
      <usgs>197.346511841</usgs>
    </waypoint>
    <waypoint id='2596'>
      <lat>29.729038</lat>
      <lon>-98.117167</lon>
      <ele>197.2</ele>
      <usgs>197.545455933</usgs>
    </waypoint>
    <waypoint id='2597'>
      <lat>29.729795</lat>
      <lon>-98.116734</lon>
      <ele>197.7</ele>
      <usgs>196.853347778</usgs>
    </waypoint>
    <waypoint id='2598'>
      <lat>29.730467</lat>
      <lon>-98.116345</lon>
      <ele>199.1</ele>
      <usgs>200.308792114</usgs>
    </waypoint>
    <waypoint id='2599'>
      <lat>29.731026</lat>
      <lon>-98.116033</lon>
      <ele>199.6</ele>
      <usgs>200.675842285</usgs>
    </waypoint>
    <waypoint id='2600'>
      <lat>29.73163</lat>
      <lon>-98.115744</lon>
      <ele>200.1</ele>
      <usgs>201.46786499</usgs>
    </waypoint>
    <waypoint id='2601'>
      <lat>29.7321</lat>
      <lon>-98.115476</lon>
      <ele>200.1</ele>
      <usgs>201.980148315</usgs>
    </waypoint>
    <waypoint id='2602'>
      <lat>29.732405</lat>
      <lon>-98.11515</lon>
      <ele>200.6</ele>
      <usgs>201.711700439</usgs>
    </waypoint>
    <waypoint id='2603'>
      <lat>29.732874</lat>
      <lon>-98.114567</lon>
      <ele>200.6</ele>
      <usgs>201.875335693</usgs>
    </waypoint>
    <waypoint id='2604'>
      <lat>29.733176</lat>
      <lon>-98.11418</lon>
      <ele>200.6</ele>
      <usgs>201.842178345</usgs>
    </waypoint>
    <waypoint id='2605'>
      <lat>29.733522</lat>
      <lon>-98.11369</lon>
      <ele>200.6</ele>
      <usgs>201.866287231</usgs>
    </waypoint>
    <waypoint id='2606'>
      <lat>29.733763</lat>
      <lon>-98.113259</lon>
      <ele>200.6</ele>
      <usgs>201.812896729</usgs>
    </waypoint>
    <waypoint id='2607'>
      <lat>29.733918</lat>
      <lon>-98.112908</lon>
      <ele>200.6</ele>
      <usgs>201.81980896</usgs>
    </waypoint>
    <waypoint id='2608'>
      <lat>29.734154</lat>
      <lon>-98.11229</lon>
      <ele>200.6</ele>
      <usgs>201.526062012</usgs>
    </waypoint>
    <waypoint id='2609'>
      <lat>29.734353</lat>
      <lon>-98.11193</lon>
      <ele>198.6</ele>
      <usgs>197.754684448</usgs>
    </waypoint>
    <waypoint id='2610'>
      <lat>29.734669</lat>
      <lon>-98.111415</lon>
      <ele>197.7</ele>
      <usgs>196.933502197</usgs>
    </waypoint>
    <waypoint id='2611'>
      <lat>29.735039</lat>
      <lon>-98.110812</lon>
      <ele>196.7</ele>
      <usgs>195.683547974</usgs>
    </waypoint>
    <waypoint id='2612'>
      <lat>29.735242</lat>
      <lon>-98.110489</lon>
      <ele>195.8</ele>
      <usgs>195.598327637</usgs>
    </waypoint>
    <waypoint id='2613'>
      <lat>29.735637</lat>
      <lon>-98.109865</lon>
      <ele>195.3</ele>
      <usgs>195.567550659</usgs>
    </waypoint>
    <waypoint id='2614'>
      <lat>29.7362</lat>
      <lon>-98.108973</lon>
      <ele>192.4</ele>
      <usgs>192.496276855</usgs>
    </waypoint>
    <waypoint id='2615'>
      <lat>29.736256</lat>
      <lon>-98.108888</lon>
      <ele>191.9</ele>
      <usgs>192.42515564</usgs>
    </waypoint>
    <waypoint id='2616'>
      <lat>29.736706</lat>
      <lon>-98.108188</lon>
      <ele>189.0</ele>
      <usgs>189.701889038</usgs>
    </waypoint>
    <waypoint id='2617'>
      <lat>29.736932</lat>
      <lon>-98.107836</lon>
      <ele>188.1</ele>
      <usgs>188.672592163</usgs>
    </waypoint>
    <waypoint id='2618'>
      <lat>29.73749</lat>
      <lon>-98.106977</lon>
      <ele>186.2</ele>
      <usgs>186.038406372</usgs>
    </waypoint>
    <waypoint id='2619'>
      <lat>29.737831</lat>
      <lon>-98.106457</lon>
      <ele>184.7</ele>
      <usgs>184.709594727</usgs>
    </waypoint>
    <waypoint id='2620'>
      <lat>29.737874</lat>
      <lon>-98.106404</lon>
      <ele>184.7</ele>
      <usgs>184.556640625</usgs>
    </waypoint>
    <waypoint id='2621'>
      <lat>29.738208</lat>
      <lon>-98.106206</lon>
      <ele>185.2</ele>
      <usgs>183.903320312</usgs>
    </waypoint>
    <waypoint id='2622'>
      <lat>29.738514</lat>
      <lon>-98.106064</lon>
      <ele>185.2</ele>
      <usgs>184.802017212</usgs>
    </waypoint>
    <waypoint id='2623'>
      <lat>29.738732</lat>
      <lon>-98.105898</lon>
      <ele>186.6</ele>
      <usgs>189.401412964</usgs>
    </waypoint>
    <waypoint id='2624'>
      <lat>29.738844</lat>
      <lon>-98.105752</lon>
      <ele>189.5</ele>
      <usgs>192.007278442</usgs>
    </waypoint>
    <waypoint id='2625'>
      <lat>29.738893</lat>
      <lon>-98.105596</lon>
      <ele>192.4</ele>
      <usgs>195.480300903</usgs>
    </waypoint>
    <waypoint id='2626'>
      <lat>29.738975</lat>
      <lon>-98.105424</lon>
      <ele>195.8</ele>
      <usgs>197.070358276</usgs>
    </waypoint>
    <waypoint id='2627'>
      <lat>29.738992</lat>
      <lon>-98.105395</lon>
      <ele>196.2</ele>
      <usgs>197.665756226</usgs>
    </waypoint>
    <waypoint id='2628'>
      <lat>29.739071</lat>
      <lon>-98.105201</lon>
      <ele>197.7</ele>
      <usgs>199.484909058</usgs>
    </waypoint>
    <waypoint id='2629'>
      <lat>29.739128</lat>
      <lon>-98.104978</lon>
      <ele>199.6</ele>
      <usgs>202.199508667</usgs>
    </waypoint>
    <waypoint id='2630'>
      <lat>29.739077</lat>
      <lon>-98.104794</lon>
      <ele>201.1</ele>
      <usgs>203.658554077</usgs>
    </waypoint>
    <waypoint id='2631'>
      <lat>29.738934</lat>
      <lon>-98.104674</lon>
      <ele>201.5</ele>
      <usgs>204.498321533</usgs>
    </waypoint>
    <waypoint id='2632'>
      <lat>29.738663</lat>
      <lon>-98.104459</lon>
      <ele>203.0</ele>
      <usgs>205.191009521</usgs>
    </waypoint>
    <waypoint id='2633'>
      <lat>29.738411</lat>
      <lon>-98.104231</lon>
      <ele>203.9</ele>
      <usgs>205.80581665</usgs>
    </waypoint>
    <waypoint id='2634'>
      <lat>29.738289</lat>
      <lon>-98.104074</lon>
      <ele>203.5</ele>
      <usgs>206.126815796</usgs>
    </waypoint>
  </segment>

  <turn id='50'>
    <fromto>Hunter Rd. to Gruene Rd.</fromto>
    <cue>RIGHT onto Gruene Rd.</cue>
    <comments>Hunter Rd. dead-ends into Gruene Rd. in Gruene right in front of
      Gruene Hall.</comments>
  </turn>

  <segment id='50'>
    <road>Gruene Rd.</road>
    <fromto>Hunter Rd. to Torrey St.</fromto>
    <comments>You'll go almost immediately down the steep hill and over the
      river, then through woods and neighborhoods.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='1513'>
      <lat>29.738495</lat>
      <lon>-98.104334</lon>
      <ele>207.3</ele>
      <usgs>205.609481812</usgs>
    </waypoint>
    <waypoint id='1514'>
      <lat>29.73873</lat>
      <lon>-98.104517</lon>
      <ele>206.8</ele>
      <usgs>205.088104248</usgs>
    </waypoint>
    <waypoint id='1515'>
      <lat>29.739012</lat>
      <lon>-98.104763</lon>
      <ele>204.9</ele>
      <usgs>204.086273193</usgs>
    </waypoint>
    <waypoint id='1516'>
      <lat>29.739077</lat>
      <lon>-98.104967</lon>
      <ele>203.9</ele>
      <usgs>202.199508667</usgs>
    </waypoint>
    <waypoint id='1517'>
      <lat>29.739031</lat>
      <lon>-98.105179</lon>
      <ele>203.0</ele>
      <usgs>200.430969238</usgs>
    </waypoint>
    <waypoint id='1518'>
      <lat>29.738867</lat>
      <lon>-98.10565</lon>
      <ele>201.1</ele>
      <usgs>193.39831543</usgs>
    </waypoint>
    <waypoint id='1519'>
      <lat>29.738572</lat>
      <lon>-98.106043</lon>
      <ele>195.3</ele>
      <usgs>185.78338623</usgs>
    </waypoint>
    <waypoint id='1520'>
      <lat>29.738467</lat>
      <lon>-98.106114</lon>
      <ele>193.4</ele>
      <usgs>184.318557739</usgs>
    </waypoint>
    <waypoint id='1521'>
      <lat>29.737945</lat>
      <lon>-98.106398</lon>
      <ele>191.9</ele>
      <usgs>184.556640625</usgs>
    </waypoint>
    <waypoint id='1522'>
      <lat>29.737672</lat>
      <lon>-98.106713</lon>
      <ele>191.9</ele>
      <usgs>185.442016602</usgs>
    </waypoint>
    <waypoint id='1523'>
      <lat>29.737619</lat>
      <lon>-98.106793</lon>
      <ele>191.9</ele>
      <usgs>185.59161377</usgs>
    </waypoint>
    <waypoint id='1524'>
      <lat>29.737396</lat>
      <lon>-98.107129</lon>
      <ele>191.9</ele>
      <usgs>186.382339478</usgs>
    </waypoint>
    <waypoint id='1525'>
      <lat>29.737189</lat>
      <lon>-98.107439</lon>
      <ele>191.4</ele>
      <usgs>187.652130127</usgs>
    </waypoint>
    <waypoint id='1526'>
      <lat>29.736955</lat>
      <lon>-98.107792</lon>
      <ele>191.9</ele>
      <usgs>188.556686401</usgs>
    </waypoint>
    <waypoint id='1527'>
      <lat>29.736712</lat>
      <lon>-98.108177</lon>
      <ele>192.9</ele>
      <usgs>189.701889038</usgs>
    </waypoint>
    <waypoint id='1528'>
      <lat>29.736527</lat>
      <lon>-98.108469</lon>
      <ele>194.3</ele>
      <usgs>190.805282593</usgs>
    </waypoint>
    <waypoint id='1529'>
      <lat>29.736286</lat>
      <lon>-98.108854</lon>
      <ele>194.8</ele>
      <usgs>192.42515564</usgs>
    </waypoint>
    <waypoint id='1530'>
      <lat>29.736008</lat>
      <lon>-98.109294</lon>
      <ele>196.2</ele>
      <usgs>193.33001709</usgs>
    </waypoint>
    <waypoint id='1531'>
      <lat>29.735682</lat>
      <lon>-98.109797</lon>
      <ele>198.2</ele>
      <usgs>195.451477051</usgs>
    </waypoint>
    <waypoint id='1532'>
      <lat>29.735322</lat>
      <lon>-98.11034</lon>
      <ele>198.2</ele>
      <usgs>195.502563477</usgs>
    </waypoint>
    <waypoint id='1533'>
      <lat>29.73505</lat>
      <lon>-98.110744</lon>
      <ele>199.1</ele>
      <usgs>195.683547974</usgs>
    </waypoint>
    <waypoint id='1534'>
      <lat>29.734786</lat>
      <lon>-98.111176</lon>
      <ele>199.1</ele>
      <usgs>196.225784302</usgs>
    </waypoint>
    <waypoint id='1535'>
      <lat>29.734538</lat>
      <lon>-98.111591</lon>
      <ele>199.1</ele>
      <usgs>197.443710327</usgs>
    </waypoint>
    <waypoint id='1536'>
      <lat>29.734352</lat>
      <lon>-98.111938</lon>
      <ele>201.1</ele>
      <usgs>197.754684448</usgs>
    </waypoint>
    <waypoint id='1537'>
      <lat>29.734099</lat>
      <lon>-98.112422</lon>
      <ele>203.5</ele>
      <usgs>201.722335815</usgs>
    </waypoint>
    <waypoint id='1538'>
      <lat>29.733912</lat>
      <lon>-98.112938</lon>
      <ele>204.4</ele>
      <usgs>201.81980896</usgs>
    </waypoint>
    <waypoint id='1539'>
      <lat>29.733697</lat>
      <lon>-98.113424</lon>
      <ele>203.9</ele>
      <usgs>201.705429077</usgs>
    </waypoint>
    <waypoint id='1540'>
      <lat>29.733486</lat>
      <lon>-98.11375</lon>
      <ele>204.4</ele>
      <usgs>201.761520386</usgs>
    </waypoint>
    <waypoint id='1541'>
      <lat>29.733106</lat>
      <lon>-98.114275</lon>
      <ele>205.4</ele>
      <usgs>201.809341431</usgs>
    </waypoint>
    <waypoint id='1542'>
      <lat>29.732613</lat>
      <lon>-98.114893</lon>
      <ele>205.9</ele>
      <usgs>201.733215332</usgs>
    </waypoint>
    <waypoint id='1543'>
      <lat>29.732169</lat>
      <lon>-98.115428</lon>
      <ele>205.4</ele>
      <usgs>201.923919678</usgs>
    </waypoint>
    <waypoint id='1544'>
      <lat>29.731896</lat>
      <lon>-98.115631</lon>
      <ele>205.4</ele>
      <usgs>201.897079468</usgs>
    </waypoint>
    <waypoint id='1545'>
      <lat>29.731415</lat>
      <lon>-98.11588</lon>
      <ele>204.4</ele>
      <usgs>200.901672363</usgs>
    </waypoint>
    <waypoint id='1546'>
      <lat>29.73066</lat>
      <lon>-98.116254</lon>
      <ele>203.5</ele>
      <usgs>200.475463867</usgs>
    </waypoint>
    <waypoint id='1547'>
      <lat>29.730131</lat>
      <lon>-98.116569</lon>
      <ele>202.0</ele>
      <usgs>197.47442627</usgs>
    </waypoint>
    <waypoint id='1548'>
      <lat>29.729541</lat>
      <lon>-98.116918</lon>
      <ele>199.6</ele>
      <usgs>197.607223511</usgs>
    </waypoint>
    <waypoint id='1549'>
      <lat>29.728907</lat>
      <lon>-98.117295</lon>
      <ele>201.1</ele>
      <usgs>197.685348511</usgs>
    </waypoint>
    <waypoint id='1550'>
      <lat>29.728054</lat>
      <lon>-98.117798</lon>
      <ele>201.5</ele>
      <usgs>197.58555603</usgs>
    </waypoint>
    <waypoint id='1551'>
      <lat>29.727234</lat>
      <lon>-98.118289</lon>
      <ele>201.1</ele>
      <usgs>197.820846558</usgs>
    </waypoint>
    <waypoint id='1552'>
      <lat>29.726636</lat>
      <lon>-98.118653</lon>
      <ele>201.1</ele>
      <usgs>198.150238037</usgs>
    </waypoint>
    <waypoint id='1553'>
      <lat>29.725753</lat>
      <lon>-98.119186</lon>
      <ele>199.6</ele>
      <usgs>197.968658447</usgs>
    </waypoint>
    <waypoint id='1554'>
      <lat>29.725696</lat>
      <lon>-98.119216</lon>
      <ele>199.6</ele>
      <usgs>197.579330444</usgs>
    </waypoint>
    <waypoint id='1555'>
      <lat>29.725453</lat>
      <lon>-98.119233</lon>
      <ele>199.1</ele>
      <usgs>196.213348389</usgs>
    </waypoint>
    <waypoint id='1556'>
      <lat>29.725295</lat>
      <lon>-98.11911</lon>
      <ele>198.2</ele>
      <usgs>196.047363281</usgs>
    </waypoint>
    <waypoint id='1557'>
      <lat>29.724869</lat>
      <lon>-98.118637</lon>
      <ele>195.8</ele>
      <usgs>193.688720703</usgs>
    </waypoint>
    <waypoint id='1558'>
      <lat>29.724334</lat>
      <lon>-98.118041</lon>
      <ele>194.8</ele>
      <usgs>191.498794556</usgs>
    </waypoint>
    <waypoint id='1559'>
      <lat>29.723949</lat>
      <lon>-98.117622</lon>
      <ele>192.9</ele>
      <usgs>190.708312988</usgs>
    </waypoint>
  </segment>

  <turn id='76'>
    <fromto>parking to Gruene Rd.</fromto>
    <cue>LEFT onto Gruene Rd.</cue>
    <comments>From parking turn left (southeast) onto Gruene Rd.</comments>
  </turn>

  <segment id='76'>
    <road>Gruene Rd.</road>
    <fromto>parking to Post Rd.</fromto>
    <comments>This road takes you out of Gruene and into New Braunfels
      neighborhoods.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>35</speed>
    <waypoint id='3060' stop='0a'>
      <lat>29.738141</lat>
      <lon>-98.104013</lon>
      <ele>203.5</ele>
      <usgs>206.126251221</usgs>
    </waypoint>
    <waypoint id='3061'>
      <lat>29.737878</lat>
      <lon>-98.103828</lon>
      <ele>203.5</ele>
      <usgs>206.345718384</usgs>
    </waypoint>
    <waypoint id='3062'>
      <lat>29.737575</lat>
      <lon>-98.103621</lon>
      <ele>203.5</ele>
      <usgs>206.544708252</usgs>
    </waypoint>
    <waypoint id='3063'>
      <lat>29.737329</lat>
      <lon>-98.103462</lon>
      <ele>203.5</ele>
      <usgs>206.678878784</usgs>
    </waypoint>
    <waypoint id='3064'>
      <lat>29.736982</lat>
      <lon>-98.103257</lon>
      <ele>203.0</ele>
      <usgs>206.326568604</usgs>
    </waypoint>
    <waypoint id='3065'>
      <lat>29.736599</lat>
      <lon>-98.103045</lon>
      <ele>202.5</ele>
      <usgs>206.088302612</usgs>
    </waypoint>
    <waypoint id='3066'>
      <lat>29.736178</lat>
      <lon>-98.102915</lon>
      <ele>203.0</ele>
      <usgs>204.513290405</usgs>
    </waypoint>
    <waypoint id='3067'>
      <lat>29.735748</lat>
      <lon>-98.102894</lon>
      <ele>203.9</ele>
      <usgs>205.38230896</usgs>
    </waypoint>
    <waypoint id='3068'>
      <lat>29.735346</lat>
      <lon>-98.102972</lon>
      <ele>203.0</ele>
      <usgs>205.090270996</usgs>
    </waypoint>
    <waypoint id='3069'>
      <lat>29.734636</lat>
      <lon>-98.103136</lon>
      <ele>203.5</ele>
      <usgs>205.690719604</usgs>
    </waypoint>
    <waypoint id='3070'>
      <lat>29.733965</lat>
      <lon>-98.103266</lon>
      <ele>204.4</ele>
      <usgs>205.575805664</usgs>
    </waypoint>
    <waypoint id='3071'>
      <lat>29.733209</lat>
      <lon>-98.103344</lon>
      <ele>204.4</ele>
      <usgs>204.987457275</usgs>
    </waypoint>
    <waypoint id='3072'>
      <lat>29.732545</lat>
      <lon>-98.103415</lon>
      <ele>204.4</ele>
      <usgs>205.1665802</usgs>
    </waypoint>
    <waypoint id='3073'>
      <lat>29.731869</lat>
      <lon>-98.103499</lon>
      <ele>204.4</ele>
      <usgs>205.516876221</usgs>
    </waypoint>
    <waypoint id='3074'>
      <lat>29.731316</lat>
      <lon>-98.103579</lon>
      <ele>203.9</ele>
      <usgs>204.625183105</usgs>
    </waypoint>
    <waypoint id='3075'>
      <lat>29.730875</lat>
      <lon>-98.103758</lon>
      <ele>201.5</ele>
      <usgs>203.421279907</usgs>
    </waypoint>
    <waypoint id='3076'>
      <lat>29.730485</lat>
      <lon>-98.104033</lon>
      <ele>200.1</ele>
      <usgs>202.370635986</usgs>
    </waypoint>
    <waypoint id='3077'>
      <lat>29.730107</lat>
      <lon>-98.104263</lon>
      <ele>200.1</ele>
      <usgs>201.873260498</usgs>
    </waypoint>
    <waypoint id='3078'>
      <lat>29.729994</lat>
      <lon>-98.10431</lon>
      <ele>199.6</ele>
      <usgs>202.007751465</usgs>
    </waypoint>
    <waypoint id='3079'>
      <lat>29.729592</lat>
      <lon>-98.104403</lon>
      <ele>199.6</ele>
      <usgs>202.160705566</usgs>
    </waypoint>
    <waypoint id='3080'>
      <lat>29.729133</lat>
      <lon>-98.104388</lon>
      <ele>199.6</ele>
      <usgs>202.266067505</usgs>
    </waypoint>
    <waypoint id='3081'>
      <lat>29.728615</lat>
      <lon>-98.104244</lon>
      <ele>199.1</ele>
      <usgs>202.467590332</usgs>
    </waypoint>
    <waypoint id='3082'>
      <lat>29.72767</lat>
      <lon>-98.103954</lon>
      <ele>197.7</ele>
      <usgs>201.941833496</usgs>
    </waypoint>
    <waypoint id='3083'>
      <lat>29.726904</lat>
      <lon>-98.103717</lon>
      <ele>197.7</ele>
      <usgs>200.912628174</usgs>
    </waypoint>
    <waypoint id='3084'>
      <lat>29.726256</lat>
      <lon>-98.103512</lon>
      <ele>196.7</ele>
      <usgs>200.672348022</usgs>
    </waypoint>
    <waypoint id='3085'>
      <lat>29.725484</lat>
      <lon>-98.103277</lon>
      <ele>196.2</ele>
      <usgs>201.551879883</usgs>
    </waypoint>
    <waypoint id='3086'>
      <lat>29.724945</lat>
      <lon>-98.103062</lon>
      <ele>197.7</ele>
      <usgs>201.837417603</usgs>
    </waypoint>
    <waypoint id='3087'>
      <lat>29.724548</lat>
      <lon>-98.102772</lon>
      <ele>197.7</ele>
      <usgs>202.253677368</usgs>
    </waypoint>
    <waypoint id='3088'>
      <lat>29.72388</lat>
      <lon>-98.102211</lon>
      <ele>198.2</ele>
      <usgs>203.234695435</usgs>
    </waypoint>
    <waypoint id='3089'>
      <lat>29.72332</lat>
      <lon>-98.10175</lon>
      <ele>198.2</ele>
      <usgs>203.845352173</usgs>
    </waypoint>
    <waypoint id='3090'>
      <lat>29.722728</lat>
      <lon>-98.101261</lon>
      <ele>199.6</ele>
      <usgs>204.493850708</usgs>
    </waypoint>
    <waypoint id='3091'>
      <lat>29.72241</lat>
      <lon>-98.101</lon>
      <ele>198.6</ele>
      <usgs>204.620529175</usgs>
    </waypoint>
    <waypoint id='3092'>
      <lat>29.722283</lat>
      <lon>-98.100898</lon>
      <ele>198.2</ele>
      <usgs>204.774169922</usgs>
    </waypoint>
    <waypoint id='3093'>
      <lat>29.722244</lat>
      <lon>-98.100862</lon>
      <ele>198.2</ele>
      <usgs>204.774169922</usgs>
    </waypoint>
    <waypoint id='3094'>
      <lat>29.722248</lat>
      <lon>-98.100874</lon>
      <ele>198.2</ele>
      <usgs>204.774169922</usgs>
    </waypoint>
    <waypoint id='3095'>
      <lat>29.722193</lat>
      <lon>-98.100829</lon>
      <ele>198.6</ele>
      <usgs>204.943893433</usgs>
    </waypoint>
    <waypoint id='3096' stop='10'>
      <lat>29.722023</lat>
      <lon>-98.10069</lon>
      <ele>200.1</ele>
      <usgs>205.146621704</usgs>
    </waypoint>
    <waypoint id='3097'>
      <lat>29.721657</lat>
      <lon>-98.10038</lon>
      <ele>200.1</ele>
      <usgs>205.474304199</usgs>
    </waypoint>
    <waypoint id='3098'>
      <lat>29.721232</lat>
      <lon>-98.100024</lon>
      <ele>200.6</ele>
      <usgs>205.655548096</usgs>
    </waypoint>
    <waypoint id='3099'>
      <lat>29.720828</lat>
      <lon>-98.099687</lon>
      <ele>201.1</ele>
      <usgs>205.942596436</usgs>
    </waypoint>
    <waypoint id='3100'>
      <lat>29.720394</lat>
      <lon>-98.099327</lon>
      <ele>201.1</ele>
      <usgs>206.157089233</usgs>
    </waypoint>
    <waypoint id='3101'>
      <lat>29.719881</lat>
      <lon>-98.098902</lon>
      <ele>201.5</ele>
      <usgs>206.31918335</usgs>
    </waypoint>
    <waypoint id='3102'>
      <lat>29.719335</lat>
      <lon>-98.098452</lon>
      <ele>202.0</ele>
      <usgs>206.358673096</usgs>
    </waypoint>
    <waypoint id='3103'>
      <lat>29.718763</lat>
      <lon>-98.097986</lon>
      <ele>201.5</ele>
      <usgs>206.260375977</usgs>
    </waypoint>
    <waypoint id='3104'>
      <lat>29.718242</lat>
      <lon>-98.097555</lon>
      <ele>201.1</ele>
      <usgs>205.817398071</usgs>
    </waypoint>
    <waypoint id='3105'>
      <lat>29.717723</lat>
      <lon>-98.097123</lon>
      <ele>201.5</ele>
      <usgs>205.14743042</usgs>
    </waypoint>
    <waypoint id='3106'>
      <lat>29.717356</lat>
      <lon>-98.096815</lon>
      <ele>201.5</ele>
      <usgs>204.532196045</usgs>
    </waypoint>
    <waypoint id='3107'>
      <lat>29.716825</lat>
      <lon>-98.096382</lon>
      <ele>201.1</ele>
      <usgs>204.408950806</usgs>
    </waypoint>
    <waypoint id='3108'>
      <lat>29.716411</lat>
      <lon>-98.09603</lon>
      <ele>200.6</ele>
      <usgs>204.43963623</usgs>
    </waypoint>
    <waypoint id='3109'>
      <lat>29.716017</lat>
      <lon>-98.095704</lon>
      <ele>199.6</ele>
      <usgs>204.335281372</usgs>
    </waypoint>
    <waypoint id='3110'>
      <lat>29.7156</lat>
      <lon>-98.095356</lon>
      <ele>199.6</ele>
      <usgs>204.159454346</usgs>
    </waypoint>
    <waypoint id='3111'>
      <lat>29.715377</lat>
      <lon>-98.095165</lon>
      <ele>197.7</ele>
      <usgs>204.140289307</usgs>
    </waypoint>
  </segment>

  <turn id='77'>
    <fromto>Gruene Rd. to Post Rd.</fromto>
    <cue>RIGHT onto Post Rd.</cue>
    <comments>Gruene Rd. dead-ends into Post Rd.</comments>
  </turn>

  <segment id='77'>
    <road>Post Rd.</road>
    <fromto>Gruene Rd. to Church Hill Dr.</fromto>
    <comments>You'll ride beside the railroad tracks.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3112'>
      <lat>29.715216</lat>
      <lon>-98.095153</lon>
      <ele>198.6</ele>
      <usgs>204.074935913</usgs>
    </waypoint>
    <waypoint id='3113'>
      <lat>29.715178</lat>
      <lon>-98.095194</lon>
      <ele>198.6</ele>
      <usgs>204.027587891</usgs>
    </waypoint>
    <waypoint id='3114'>
      <lat>29.71478</lat>
      <lon>-98.095661</lon>
      <ele>199.6</ele>
      <usgs>203.822982788</usgs>
    </waypoint>
    <waypoint id='3115'>
      <lat>29.714699</lat>
      <lon>-98.095752</lon>
      <ele>198.6</ele>
      <usgs>203.784439087</usgs>
    </waypoint>
    <waypoint id='3116'>
      <lat>29.714237</lat>
      <lon>-98.096272</lon>
      <ele>198.6</ele>
      <usgs>203.617721558</usgs>
    </waypoint>
    <waypoint id='3117'>
      <lat>29.713656</lat>
      <lon>-98.096906</lon>
      <ele>198.2</ele>
      <usgs>203.200790405</usgs>
    </waypoint>
    <waypoint id='3118'>
      <lat>29.713262</lat>
      <lon>-98.097251</lon>
      <ele>198.6</ele>
      <usgs>202.892593384</usgs>
    </waypoint>
    <waypoint id='3119'>
      <lat>29.712757</lat>
      <lon>-98.097524</lon>
      <ele>198.2</ele>
      <usgs>202.698348999</usgs>
    </waypoint>
    <waypoint id='3120'>
      <lat>29.712005</lat>
      <lon>-98.097923</lon>
      <ele>197.2</ele>
      <usgs>202.194778442</usgs>
    </waypoint>
    <waypoint id='3121'>
      <lat>29.711601</lat>
      <lon>-98.098139</lon>
      <ele>196.7</ele>
      <usgs>201.980804443</usgs>
    </waypoint>
    <waypoint id='3122'>
      <lat>29.710952</lat>
      <lon>-98.098491</lon>
      <ele>197.7</ele>
      <usgs>201.249481201</usgs>
    </waypoint>
    <waypoint id='3123'>
      <lat>29.710246</lat>
      <lon>-98.098867</lon>
      <ele>195.8</ele>
      <usgs>200.622909546</usgs>
    </waypoint>
    <waypoint id='3124'>
      <lat>29.709638</lat>
      <lon>-98.099162</lon>
      <ele>194.8</ele>
      <usgs>199.901519775</usgs>
    </waypoint>
  </segment>

  <turn id='78'>
    <fromto>Post Rd. to Church Hill Dr.</fromto>
    <cue>LEFT onto Church Hill Dr.</cue>
    <comments>Post Rd. dead-ends into Church Hill Dr.</comments>
  </turn>

  <segment id='78'>
    <road>Church Hill Dr.</road>
    <fromto>Post Rd. to Rusk Ave.</fromto>
    <comments>Wind around and go under Loop 337.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3125'>
      <lat>29.709392</lat>
      <lon>-98.099298</lon>
      <ele>194.8</ele>
      <usgs>198.990447998</usgs>
    </waypoint>
    <waypoint id='3126'>
      <lat>29.709209</lat>
      <lon>-98.099251</lon>
      <ele>194.8</ele>
      <usgs>199.476791382</usgs>
    </waypoint>
    <waypoint id='3127'>
      <lat>29.708868</lat>
      <lon>-98.099059</lon>
      <ele>195.8</ele>
      <usgs>200.564224243</usgs>
    </waypoint>
    <waypoint id='3128'>
      <lat>29.708541</lat>
      <lon>-98.098868</lon>
      <ele>195.3</ele>
      <usgs>200.585540771</usgs>
    </waypoint>
    <waypoint id='3129'>
      <lat>29.708123</lat>
      <lon>-98.098494</lon>
      <ele>194.3</ele>
      <usgs>199.983200073</usgs>
    </waypoint>
    <waypoint id='3130'>
      <lat>29.70769</lat>
      <lon>-98.097985</lon>
      <ele>194.3</ele>
      <usgs>199.525619507</usgs>
    </waypoint>
    <waypoint id='3131'>
      <lat>29.707455</lat>
      <lon>-98.097764</lon>
      <ele>194.3</ele>
      <usgs>199.057769775</usgs>
    </waypoint>
    <waypoint id='3132'>
      <lat>29.707133</lat>
      <lon>-98.097679</lon>
      <ele>194.8</ele>
      <usgs>198.675231934</usgs>
    </waypoint>
    <waypoint id='3133'>
      <lat>29.707066</lat>
      <lon>-98.097686</lon>
      <ele>195.8</ele>
      <usgs>198.262954712</usgs>
    </waypoint>
    <waypoint id='3134'>
      <lat>29.706814</lat>
      <lon>-98.097749</lon>
      <ele>193.8</ele>
      <usgs>196.945297241</usgs>
    </waypoint>
    <waypoint id='3135'>
      <lat>29.706514</lat>
      <lon>-98.097859</lon>
      <ele>193.8</ele>
      <usgs>196.833190918</usgs>
    </waypoint>
    <waypoint id='3136'>
      <lat>29.706314</lat>
      <lon>-98.098014</lon>
      <ele>194.8</ele>
      <usgs>197.320281982</usgs>
    </waypoint>
    <waypoint id='3137'>
      <lat>29.705851</lat>
      <lon>-98.098549</lon>
      <ele>193.4</ele>
      <usgs>196.749740601</usgs>
    </waypoint>
    <waypoint id='3138'>
      <lat>29.705585</lat>
      <lon>-98.098851</lon>
      <ele>191.9</ele>
      <usgs>195.115219116</usgs>
    </waypoint>
    <waypoint id='3139'>
      <lat>29.7053</lat>
      <lon>-98.099164</lon>
      <ele>190.0</ele>
      <usgs>193.513381958</usgs>
    </waypoint>
    <waypoint id='3140'>
      <lat>29.704773</lat>
      <lon>-98.099751</lon>
      <ele>188.6</ele>
      <usgs>191.088684082</usgs>
    </waypoint>
    <waypoint id='3141'>
      <lat>29.704276</lat>
      <lon>-98.100294</lon>
      <ele>187.6</ele>
      <usgs>190.476242065</usgs>
    </waypoint>
    <waypoint id='3142'>
      <lat>29.703874</lat>
      <lon>-98.10073</lon>
      <ele>185.7</ele>
      <usgs>190.354492188</usgs>
    </waypoint>
    <waypoint id='3143'>
      <lat>29.703453</lat>
      <lon>-98.101207</lon>
      <ele>185.2</ele>
      <usgs>190.314529419</usgs>
    </waypoint>
    <waypoint id='3144'>
      <lat>29.703023</lat>
      <lon>-98.101684</lon>
      <ele>185.2</ele>
      <usgs>190.283035278</usgs>
    </waypoint>
    <waypoint id='3145'>
      <lat>29.702701</lat>
      <lon>-98.102046</lon>
      <ele>186.2</ele>
      <usgs>190.333358765</usgs>
    </waypoint>
    <waypoint id='3146'>
      <lat>29.702013</lat>
      <lon>-98.102815</lon>
      <ele>185.7</ele>
      <usgs>190.411529541</usgs>
    </waypoint>
    <waypoint id='3147'>
      <lat>29.7015</lat>
      <lon>-98.103363</lon>
      <ele>186.2</ele>
      <usgs>190.49810791</usgs>
    </waypoint>
    <waypoint id='3148'>
      <lat>29.701451</lat>
      <lon>-98.103409</lon>
      <ele>186.6</ele>
      <usgs>190.444290161</usgs>
    </waypoint>
    <waypoint id='3149'>
      <lat>29.701351</lat>
      <lon>-98.103497</lon>
      <ele>185.2</ele>
      <usgs>190.45475769</usgs>
    </waypoint>
    <waypoint id='3150'>
      <lat>29.701152</lat>
      <lon>-98.103671</lon>
      <ele>186.6</ele>
      <usgs>190.465957642</usgs>
    </waypoint>
    <waypoint id='3151'>
      <lat>29.700678</lat>
      <lon>-98.10409</lon>
      <ele>186.6</ele>
      <usgs>190.553222656</usgs>
    </waypoint>
    <waypoint id='3152'>
      <lat>29.700631</lat>
      <lon>-98.104132</lon>
      <ele>186.6</ele>
      <usgs>190.491027832</usgs>
    </waypoint>
    <waypoint id='3153'>
      <lat>29.700294</lat>
      <lon>-98.104425</lon>
      <ele>184.7</ele>
      <usgs>190.541244507</usgs>
    </waypoint>
    <waypoint id='3154'>
      <lat>29.700225</lat>
      <lon>-98.104482</lon>
      <ele>184.7</ele>
      <usgs>190.561447144</usgs>
    </waypoint>
  </segment>

  <turn id='79'>
    <fromto>Church Hill Dr. to Rusk Ave.</fromto>
    <cue>LEFT onto Rusk Ave.</cue>
    <comments>Church Hill Dr. dead-ends into Rusk Ave.</comments>
  </turn>

  <segment id='79'>
    <road>Rusk Ave.</road>
    <fromto>Church Hill Dr. to Porter St.</fromto>
    <comments>This is a short connector street.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3155'>
      <lat>29.700056</lat>
      <lon>-98.104502</lon>
      <ele>184.7</ele>
      <usgs>190.46736145</usgs>
    </waypoint>
    <waypoint id='3156'>
      <lat>29.699864</lat>
      <lon>-98.104393</lon>
      <ele>185.7</ele>
      <usgs>190.340698242</usgs>
    </waypoint>
    <waypoint id='3157'>
      <lat>29.69955</lat>
      <lon>-98.10404</lon>
      <ele>184.2</ele>
      <usgs>189.801940918</usgs>
    </waypoint>
    <waypoint id='3158'>
      <lat>29.699368</lat>
      <lon>-98.103817</lon>
      <ele>184.7</ele>
      <usgs>189.419845581</usgs>
    </waypoint>
  </segment>

  <turn id='80'>
    <fromto>Rusk Ave. to Porter St.</fromto>
    <cue>RIGHT onto Porter St.</cue>
    <comments></comments>
  </turn>

  <segment id='80'>
    <road>Porter St.</road>
    <fromto>Rusk Ave. to bridge</fromto>
    <comments>This road runs into the old bridge over the river.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3159'>
      <lat>29.699188</lat>
      <lon>-98.10377</lon>
      <ele>185.2</ele>
      <usgs>189.24281311</usgs>
    </waypoint>
    <waypoint id='3160'>
      <lat>29.699107</lat>
      <lon>-98.103866</lon>
      <ele>185.7</ele>
      <usgs>189.259475708</usgs>
    </waypoint>
    <waypoint id='3161'>
      <lat>29.698667</lat>
      <lon>-98.104368</lon>
      <ele>185.2</ele>
      <usgs>188.97114563</usgs>
    </waypoint>
    <waypoint id='3162'>
      <lat>29.698239</lat>
      <lon>-98.104844</lon>
      <ele>185.7</ele>
      <usgs>188.360671997</usgs>
    </waypoint>
    <waypoint id='3163'>
      <lat>29.697827</lat>
      <lon>-98.105309</lon>
      <ele>184.7</ele>
      <usgs>188.063430786</usgs>
    </waypoint>
    <waypoint id='3164'>
      <lat>29.697507</lat>
      <lon>-98.105705</lon>
      <ele>185.2</ele>
      <usgs>189.391845703</usgs>
    </waypoint>
  </segment>

  <turn id='80a'>
    <fromto>Porter St. to pedestrian bridge</fromto>
    <cue>STRAIGHT onto pedestrian bridge</cue>
    <comments>Go onto the bridge instead of turning left.</comments>
  </turn>

  <segment id='80a'>
    <road>pedestrian bridge</road>
    <fromto>Porter St. to Faust St.</fromto>
    <comments>This is an old bridge that's been converted to foot and bike
      traffic.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>None</traffic>
    <speed>5</speed>
    <waypoint id='3165'>
      <lat>29.697408</lat>
      <lon>-98.105989</lon>
      <ele>185.2</ele>
      <usgs>189.101715088</usgs>
    </waypoint>
    <waypoint id='3166'>
      <lat>29.697348</lat>
      <lon>-98.106355</lon>
      <ele>185.7</ele>
      <usgs>181.687438965</usgs>
    </waypoint>
    <waypoint id='3167'>
      <lat>29.69728</lat>
      <lon>-98.106728</lon>
      <ele>186.2</ele>
      <usgs>176.256713867</usgs>
    </waypoint>
    <waypoint id='3168'>
      <lat>29.697218</lat>
      <lon>-98.107005</lon>
      <ele>187.6</ele>
      <usgs>176.257064819</usgs>
    </waypoint>
    <waypoint id='3169'>
      <lat>29.697171</lat>
      <lon>-98.107244</lon>
      <ele>187.6</ele>
      <usgs>176.6847229</usgs>
    </waypoint>
    <waypoint id='3170'>
      <lat>29.697171</lat>
      <lon>-98.107276</lon>
      <ele>187.6</ele>
      <usgs>176.6847229</usgs>
    </waypoint>
    <waypoint id='3171'>
      <lat>29.697124</lat>
      <lon>-98.10736</lon>
      <ele>186.6</ele>
      <usgs>177.281524658</usgs>
    </waypoint>
    <waypoint id='3172'>
      <lat>29.69709</lat>
      <lon>-98.107477</lon>
      <ele>188.1</ele>
      <usgs>178.797195435</usgs>
    </waypoint>
    <waypoint id='3173'>
      <lat>29.697076</lat>
      <lon>-98.10757</lon>
      <ele>186.2</ele>
      <usgs>180.944335938</usgs>
    </waypoint>
    <waypoint id='3174'>
      <lat>29.69701</lat>
      <lon>-98.107934</lon>
      <ele>185.7</ele>
      <usgs>187.522064209</usgs>
    </waypoint>
  </segment>

  <turn id='81'>
    <fromto>pedestrian bridge to Faust St.</fromto>
    <cue>STRAIGHT onto Faust St.</cue>
    <comments>When you come off the bridge you are on Faust St.</comments>
  </turn>

  <segment id='81'>
    <road>Faust St.</road>
    <fromto>pedestrian bridge to Comal Ave.</fromto>
    <comments>There is actually a bike lane on Faust St.  You don't see those
      very often.</comments>
    <lanes>2</lanes>
    <shoulder>1</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3175'>
      <lat>29.69695</lat>
      <lon>-98.108212</lon>
      <ele>186.6</ele>
      <usgs>189.640106201</usgs>
    </waypoint>
    <waypoint id='3176'>
      <lat>29.696896</lat>
      <lon>-98.108421</lon>
      <ele>185.7</ele>
      <usgs>190.044784546</usgs>
    </waypoint>
    <waypoint id='3177'>
      <lat>29.696759</lat>
      <lon>-98.108732</lon>
      <ele>185.7</ele>
      <usgs>190.615509033</usgs>
    </waypoint>
    <waypoint id='3178'>
      <lat>29.696705</lat>
      <lon>-98.108876</lon>
      <ele>184.7</ele>
      <usgs>190.669448853</usgs>
    </waypoint>
    <waypoint id='3179'>
      <lat>29.696609</lat>
      <lon>-98.109052</lon>
      <ele>185.7</ele>
      <usgs>190.582763672</usgs>
    </waypoint>
    <waypoint id='3180'>
      <lat>29.696427</lat>
      <lon>-98.10945</lon>
      <ele>184.7</ele>
      <usgs>190.036346436</usgs>
    </waypoint>
    <waypoint id='3181'>
      <lat>29.69615</lat>
      <lon>-98.110013</lon>
      <ele>184.7</ele>
      <usgs>189.115905762</usgs>
    </waypoint>
    <waypoint id='3182'>
      <lat>29.695977</lat>
      <lon>-98.11038</lon>
      <ele>184.2</ele>
      <usgs>187.6690979</usgs>
    </waypoint>
    <waypoint id='3183'>
      <lat>29.69579</lat>
      <lon>-98.11076</lon>
      <ele>184.7</ele>
      <usgs>187.135391235</usgs>
    </waypoint>
    <waypoint id='3184'>
      <lat>29.695491</lat>
      <lon>-98.111357</lon>
      <ele>184.2</ele>
      <usgs>187.481521606</usgs>
    </waypoint>
    <waypoint id='3185'>
      <lat>29.695356</lat>
      <lon>-98.11167</lon>
      <ele>183.7</ele>
      <usgs>187.884796143</usgs>
    </waypoint>
  </segment>

  <turn id='82'>
    <fromto>Faust St. to Comal Ave.</fromto>
    <cue>RIGHT onto Comal Ave.</cue>
    <comments></comments>
  </turn>

  <segment id='82'>
    <road>Comal Ave.</road>
    <fromto>Faust St. to Garden St.</fromto>
    <comments>There are some neat old houses on this road.</comments>
    <lanes>2</lanes>
    <shoulder>1</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3186'>
      <lat>29.695464</lat>
      <lon>-98.111794</lon>
      <ele>183.7</ele>
      <usgs>187.978118896</usgs>
    </waypoint>
    <waypoint id='3187'>
      <lat>29.695871</lat>
      <lon>-98.112033</lon>
      <ele>184.2</ele>
      <usgs>188.295837402</usgs>
    </waypoint>
    <waypoint id='3188'>
      <lat>29.696176</lat>
      <lon>-98.112279</lon>
      <ele>184.2</ele>
      <usgs>188.997375488</usgs>
    </waypoint>
    <waypoint id='3189'>
      <lat>29.696367</lat>
      <lon>-98.11254</lon>
      <ele>184.2</ele>
      <usgs>189.067108154</usgs>
    </waypoint>
    <waypoint id='3190'>
      <lat>29.696463</lat>
      <lon>-98.112661</lon>
      <ele>186.2</ele>
      <usgs>189.067108154</usgs>
    </waypoint>
    <waypoint id='3191'>
      <lat>29.696578</lat>
      <lon>-98.112831</lon>
      <ele>184.2</ele>
      <usgs>189.067169189</usgs>
    </waypoint>
    <waypoint id='3192'>
      <lat>29.696808</lat>
      <lon>-98.113172</lon>
      <ele>183.3</ele>
      <usgs>189.059188843</usgs>
    </waypoint>
    <waypoint id='3193'>
      <lat>29.69688</lat>
      <lon>-98.113279</lon>
      <ele>182.3</ele>
      <usgs>189.056945801</usgs>
    </waypoint>
    <waypoint id='3194'>
      <lat>29.697257</lat>
      <lon>-98.113813</lon>
      <ele>183.3</ele>
      <usgs>189.057113647</usgs>
    </waypoint>
    <waypoint id='3195'>
      <lat>29.697585</lat>
      <lon>-98.11427</lon>
      <ele>183.3</ele>
      <usgs>189.057113647</usgs>
    </waypoint>
    <waypoint id='3196'>
      <lat>29.697877</lat>
      <lon>-98.114691</lon>
      <ele>183.7</ele>
      <usgs>189.047058105</usgs>
    </waypoint>
    <waypoint id='3197'>
      <lat>29.698058</lat>
      <lon>-98.114967</lon>
      <ele>183.7</ele>
      <usgs>189.047180176</usgs>
    </waypoint>
    <waypoint id='3198'>
      <lat>29.69835</lat>
      <lon>-98.115424</lon>
      <ele>183.7</ele>
      <usgs>189.043014526</usgs>
    </waypoint>
    <waypoint id='3199'>
      <lat>29.698634</lat>
      <lon>-98.115848</lon>
      <ele>185.2</ele>
      <usgs>189.057022095</usgs>
    </waypoint>
    <waypoint id='3200'>
      <lat>29.698905</lat>
      <lon>-98.116258</lon>
      <ele>185.7</ele>
      <usgs>189.17137146</usgs>
    </waypoint>
    <waypoint id='3201'>
      <lat>29.699238</lat>
      <lon>-98.116743</lon>
      <ele>186.2</ele>
      <usgs>189.399185181</usgs>
    </waypoint>
    <waypoint id='3202'>
      <lat>29.699595</lat>
      <lon>-98.117274</lon>
      <ele>186.6</ele>
      <usgs>189.517150879</usgs>
    </waypoint>
    <waypoint id='3203'>
      <lat>29.699961</lat>
      <lon>-98.117822</lon>
      <ele>184.7</ele>
      <usgs>189.392379761</usgs>
    </waypoint>
    <waypoint id='3204'>
      <lat>29.700349</lat>
      <lon>-98.118386</lon>
      <ele>185.2</ele>
      <usgs>189.282180786</usgs>
    </waypoint>
    <waypoint id='3205'>
      <lat>29.70071</lat>
      <lon>-98.118907</lon>
      <ele>184.2</ele>
      <usgs>189.204589844</usgs>
    </waypoint>
    <waypoint id='3206'>
      <lat>29.700939</lat>
      <lon>-98.119275</lon>
      <ele>184.2</ele>
      <usgs>189.181106567</usgs>
    </waypoint>
    <waypoint id='3207'>
      <lat>29.701151</lat>
      <lon>-98.119599</lon>
      <ele>184.7</ele>
      <usgs>189.165313721</usgs>
    </waypoint>
    <waypoint id='3208'>
      <lat>29.701219</lat>
      <lon>-98.119682</lon>
      <ele>185.2</ele>
      <usgs>189.141662598</usgs>
    </waypoint>
  </segment>

  <turn id='83'>
    <fromto>Comal Ave. to Garden St./Lincoln Ave.</fromto>
    <cue>RIGHT onto Garden St.</cue>
    <comments></comments>
  </turn>

  <segment id='83'>
    <road>Garden St./Lincoln Ave.</road>
    <fromto>Comal Ave. to Union Ave.</fromto>
    <comments>Garden St. becomes Lincoln Ave. when you cross over the
      bridge.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>20</speed>
    <waypoint id='3209'>
      <lat>29.701359</lat>
      <lon>-98.119617</lon>
      <ele>184.2</ele>
      <usgs>188.690475464</usgs>
    </waypoint>
    <waypoint id='3210'>
      <lat>29.701569</lat>
      <lon>-98.119438</lon>
      <ele>184.2</ele>
      <usgs>186.927261353</usgs>
    </waypoint>
    <waypoint id='3211'>
      <lat>29.701886</lat>
      <lon>-98.11914</lon>
      <ele>181.3</ele>
      <usgs>183.083145142</usgs>
    </waypoint>
    <waypoint id='3212'>
      <lat>29.702249</lat>
      <lon>-98.118801</lon>
      <ele>180.4</ele>
      <usgs>186.202316284</usgs>
    </waypoint>
    <waypoint id='3213'>
      <lat>29.702515</lat>
      <lon>-98.118536</lon>
      <ele>181.3</ele>
      <usgs>186.920257568</usgs>
    </waypoint>
    <waypoint id='3214'>
      <lat>29.702786</lat>
      <lon>-98.118265</lon>
      <ele>182.8</ele>
      <usgs>187.309448242</usgs>
    </waypoint>
    <waypoint id='3215'>
      <lat>29.703188</lat>
      <lon>-98.117867</lon>
      <ele>183.3</ele>
      <usgs>187.775604248</usgs>
    </waypoint>
    <waypoint id='3216'>
      <lat>29.703506</lat>
      <lon>-98.117534</lon>
      <ele>184.2</ele>
      <usgs>187.767608643</usgs>
    </waypoint>
    <waypoint id='3217'>
      <lat>29.703868</lat>
      <lon>-98.11718</lon>
      <ele>184.2</ele>
      <usgs>187.630950928</usgs>
    </waypoint>
    <waypoint id='3218'>
      <lat>29.704202</lat>
      <lon>-98.116821</lon>
      <ele>184.7</ele>
      <usgs>187.458190918</usgs>
    </waypoint>
    <waypoint id='3219'>
      <lat>29.70441</lat>
      <lon>-98.116494</lon>
      <ele>183.7</ele>
      <usgs>187.307678223</usgs>
    </waypoint>
    <waypoint id='3220'>
      <lat>29.704549</lat>
      <lon>-98.116247</lon>
      <ele>183.3</ele>
      <usgs>187.216247559</usgs>
    </waypoint>
  </segment>

  <turn id='84'>
    <fromto>Lincoln Ave. to Union Ave.</fromto>
    <cue>LEFT onto Union Ave.</cue>
    <comments>There's a water park on the left corner.</comments>
  </turn>

  <segment id='84'>
    <road>Union Ave.</road>
    <fromto>Lincoln Ave. to Common St.</fromto>
    <comments>There is a water park on your left.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3221'>
      <lat>29.704727</lat>
      <lon>-98.116188</lon>
      <ele>182.8</ele>
      <usgs>187.363540649</usgs>
    </waypoint>
    <waypoint id='3222'>
      <lat>29.704821</lat>
      <lon>-98.116241</lon>
      <ele>182.8</ele>
      <usgs>187.557647705</usgs>
    </waypoint>
    <waypoint id='3223'>
      <lat>29.705278</lat>
      <lon>-98.116564</lon>
      <ele>183.3</ele>
      <usgs>188.39074707</usgs>
    </waypoint>
    <waypoint id='3224'>
      <lat>29.705671</lat>
      <lon>-98.116841</lon>
      <ele>185.2</ele>
      <usgs>189.083145142</usgs>
    </waypoint>
    <waypoint id='3225'>
      <lat>29.70572</lat>
      <lon>-98.116879</lon>
      <ele>184.7</ele>
      <usgs>189.145050049</usgs>
    </waypoint>
    <waypoint id='3226'>
      <lat>29.706061</lat>
      <lon>-98.1171</lon>
      <ele>185.7</ele>
      <usgs>189.729873657</usgs>
    </waypoint>
    <waypoint id='3227'>
      <lat>29.706414</lat>
      <lon>-98.117337</lon>
      <ele>186.6</ele>
      <usgs>189.779510498</usgs>
    </waypoint>
    <waypoint id='3228'>
      <lat>29.706921</lat>
      <lon>-98.117684</lon>
      <ele>187.1</ele>
      <usgs>190.083251953</usgs>
    </waypoint>
    <waypoint id='3229'>
      <lat>29.707469</lat>
      <lon>-98.118058</lon>
      <ele>188.1</ele>
      <usgs>191.221923828</usgs>
    </waypoint>
    <waypoint id='3230'>
      <lat>29.707884</lat>
      <lon>-98.118339</lon>
      <ele>189.5</ele>
      <usgs>193.782821655</usgs>
    </waypoint>
    <waypoint id='3231'>
      <lat>29.707991</lat>
      <lon>-98.118417</lon>
      <ele>189.0</ele>
      <usgs>194.335968018</usgs>
    </waypoint>
    <waypoint id='3232'>
      <lat>29.708038</lat>
      <lon>-98.118453</lon>
      <ele>189.5</ele>
      <usgs>194.668991089</usgs>
    </waypoint>
    <waypoint id='3233'>
      <lat>29.708175</lat>
      <lon>-98.118549</lon>
      <ele>191.0</ele>
      <usgs>195.409118652</usgs>
    </waypoint>
    <waypoint id='3234'>
      <lat>29.708498</lat>
      <lon>-98.118759</lon>
      <ele>192.4</ele>
      <usgs>195.835372925</usgs>
    </waypoint>
    <waypoint id='3235'>
      <lat>29.708916</lat>
      <lon>-98.119039</lon>
      <ele>192.4</ele>
      <usgs>196.524017334</usgs>
    </waypoint>
    <waypoint id='3236'>
      <lat>29.709259</lat>
      <lon>-98.11927</lon>
      <ele>192.9</ele>
      <usgs>197.002868652</usgs>
    </waypoint>
    <waypoint id='3237'>
      <lat>29.709335</lat>
      <lon>-98.119329</lon>
      <ele>193.8</ele>
      <usgs>197.25138855</usgs>
    </waypoint>
    <waypoint id='3238'>
      <lat>29.709618</lat>
      <lon>-98.11956</lon>
      <ele>195.3</ele>
      <usgs>197.487045288</usgs>
    </waypoint>
    <waypoint id='3239'>
      <lat>29.709736</lat>
      <lon>-98.119639</lon>
      <ele>194.8</ele>
      <usgs>197.550750732</usgs>
    </waypoint>
    <waypoint id='3240'>
      <lat>29.70975</lat>
      <lon>-98.11965</lon>
      <ele>194.8</ele>
      <usgs>197.550750732</usgs>
    </waypoint>
    <waypoint id='3241'>
      <lat>29.709761</lat>
      <lon>-98.119659</lon>
      <ele>194.8</ele>
      <usgs>197.550750732</usgs>
    </waypoint>
    <waypoint id='3242' stop='11'>
      <lat>29.709812</lat>
      <lon>-98.119746</lon>
      <ele>195.3</ele>
      <usgs>197.409164429</usgs>
    </waypoint>
  </segment>

  <turn id='85'>
    <fromto>Union Ave. to Common St.</fromto>
    <cue>LEFT onto Common St.</cue>
    <comments>Turn left at the street light.</comments>
  </turn>

  <segment id='85'>
    <road>Common St.</road>
    <fromto>Union Ave. to Hinman Island Dr.</fromto>
    <comments>Short connector between Union Ave. and Hinman Island
      Dr.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Moderate</traffic>
    <speed>30</speed>
    <waypoint id='3243'>
      <lat>29.709804</lat>
      <lon>-98.119902</lon>
      <ele>195.3</ele>
      <usgs>197.272735596</usgs>
    </waypoint>
    <waypoint id='3244'>
      <lat>29.709705</lat>
      <lon>-98.120118</lon>
      <ele>194.8</ele>
      <usgs>196.50479126</usgs>
    </waypoint>
    <waypoint id='3245'>
      <lat>29.709627</lat>
      <lon>-98.120246</lon>
      <ele>194.3</ele>
      <usgs>196.052490234</usgs>
    </waypoint>
    <waypoint id='3246'>
      <lat>29.709545</lat>
      <lon>-98.120394</lon>
      <ele>193.4</ele>
      <usgs>195.551391602</usgs>
    </waypoint>
    <waypoint id='3247'>
      <lat>29.709477</lat>
      <lon>-98.120515</lon>
      <ele>192.9</ele>
      <usgs>195.137390137</usgs>
    </waypoint>
    <waypoint id='3248'>
      <lat>29.709427</lat>
      <lon>-98.12061</lon>
      <ele>192.4</ele>
      <usgs>194.749938965</usgs>
    </waypoint>
  </segment>

  <turn id='86'>
    <fromto>Common St. to Hinman Island Dr.</fromto>
    <cue>STRAIGHT onto Hinman Island Dr.</cue>
    <comments>Common St. becomes Hinman Island Dr. as it crosses Liberty
      Ave.</comments>
  </turn>

  <segment id='86'>
    <road>Hinman Island Dr.</road>
    <fromto>Common St. to Elizabeth Ave.</fromto>
    <comments>The river is on your left and a golf course is on your right.
      This street is closed to car traffic on the weekends, so you may have to
      go around the barriers if they're up.  Bicycle traffic is OK.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>20</speed>
    <waypoint id='3249'>
      <lat>29.709467</lat>
      <lon>-98.120772</lon>
      <ele>191.9</ele>
      <usgs>194.864227295</usgs>
    </waypoint>
    <waypoint id='3250'>
      <lat>29.709503</lat>
      <lon>-98.120861</lon>
      <ele>191.0</ele>
      <usgs>194.482284546</usgs>
    </waypoint>
    <waypoint id='3251'>
      <lat>29.709449</lat>
      <lon>-98.121003</lon>
      <ele>190.5</ele>
      <usgs>193.933792114</usgs>
    </waypoint>
    <waypoint id='3252'>
      <lat>29.70948</lat>
      <lon>-98.121097</lon>
      <ele>190.0</ele>
      <usgs>193.26675415</usgs>
    </waypoint>
    <waypoint id='3253'>
      <lat>29.709627</lat>
      <lon>-98.121471</lon>
      <ele>189.0</ele>
      <usgs>190.251525879</usgs>
    </waypoint>
    <waypoint id='3254'>
      <lat>29.709749</lat>
      <lon>-98.121821</lon>
      <ele>185.2</ele>
      <usgs>184.333755493</usgs>
    </waypoint>
    <waypoint id='3255'>
      <lat>29.709811</lat>
      <lon>-98.122034</lon>
      <ele>183.7</ele>
      <usgs>182.936523438</usgs>
    </waypoint>
    <waypoint id='3256'>
      <lat>29.709813</lat>
      <lon>-98.122637</lon>
      <ele>182.3</ele>
      <usgs>185.051025391</usgs>
    </waypoint>
    <waypoint id='3257'>
      <lat>29.709699</lat>
      <lon>-98.123128</lon>
      <ele>183.3</ele>
      <usgs>185.161148071</usgs>
    </waypoint>
    <waypoint id='3258'>
      <lat>29.709627</lat>
      <lon>-98.123349</lon>
      <ele>184.7</ele>
      <usgs>185.268585205</usgs>
    </waypoint>
    <waypoint id='3259'>
      <lat>29.709428</lat>
      <lon>-98.123674</lon>
      <ele>184.2</ele>
      <usgs>186.17741394</usgs>
    </waypoint>
    <waypoint id='3260'>
      <lat>29.709095</lat>
      <lon>-98.123948</lon>
      <ele>184.2</ele>
      <usgs>186.407409668</usgs>
    </waypoint>
    <waypoint id='3261'>
      <lat>29.708706</lat>
      <lon>-98.124263</lon>
      <ele>183.7</ele>
      <usgs>187.012741089</usgs>
    </waypoint>
    <waypoint id='3262'>
      <lat>29.7086</lat>
      <lon>-98.124408</lon>
      <ele>184.2</ele>
      <usgs>186.329727173</usgs>
    </waypoint>
    <waypoint id='3263'>
      <lat>29.708423</lat>
      <lon>-98.124865</lon>
      <ele>185.2</ele>
      <usgs>186.848587036</usgs>
    </waypoint>
    <waypoint id='3264'>
      <lat>29.708291</lat>
      <lon>-98.125306</lon>
      <ele>187.6</ele>
      <usgs>187.901123047</usgs>
    </waypoint>
    <waypoint id='3265'>
      <lat>29.708196</lat>
      <lon>-98.125898</lon>
      <ele>187.6</ele>
      <usgs>188.110900879</usgs>
    </waypoint>
    <waypoint id='3266'>
      <lat>29.708216</lat>
      <lon>-98.126324</lon>
      <ele>188.1</ele>
      <usgs>190.474441528</usgs>
    </waypoint>
    <waypoint id='3267'>
      <lat>29.708271</lat>
      <lon>-98.12677</lon>
      <ele>187.1</ele>
      <usgs>190.904296875</usgs>
    </waypoint>
    <waypoint id='3268'>
      <lat>29.708344</lat>
      <lon>-98.127393</lon>
      <ele>188.1</ele>
      <usgs>190.83782959</usgs>
    </waypoint>
    <waypoint id='3269'>
      <lat>29.708414</lat>
      <lon>-98.128042</lon>
      <ele>186.6</ele>
      <usgs>190.409301758</usgs>
    </waypoint>
    <waypoint id='3270'>
      <lat>29.708497</lat>
      <lon>-98.128606</lon>
      <ele>188.1</ele>
      <usgs>190.511672974</usgs>
    </waypoint>
    <waypoint id='3271'>
      <lat>29.708511</lat>
      <lon>-98.128659</lon>
      <ele>188.1</ele>
      <usgs>190.341659546</usgs>
    </waypoint>
    <waypoint id='3272'>
      <lat>29.708621</lat>
      <lon>-98.128974</lon>
      <ele>189.5</ele>
      <usgs>190.479095459</usgs>
    </waypoint>
    <waypoint id='3273'>
      <lat>29.708695</lat>
      <lon>-98.129094</lon>
      <ele>188.6</ele>
      <usgs>190.366912842</usgs>
    </waypoint>
  </segment>

  <turn id='87'>
    <fromto>Hinman Island Dr. to Elizabeth Ave.</fromto>
    <cue>RIGHT onto Elizabeth Ave.</cue>
    <comments>Hinman Island Dr. dead-ends into Elizabeth Ave.</comments>
  </turn>

  <segment id='87'>
    <road>Elizabeth Ave.</road>
    <fromto>Hinman Island Dr. to Edgewater Terrace</fromto>
    <comments>Wind around the golf course on your left.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>20</speed>
    <waypoint id='3274'>
      <lat>29.708742</lat>
      <lon>-98.129203</lon>
      <ele>189.0</ele>
      <usgs>190.47114563</usgs>
    </waypoint>
    <waypoint id='3275'>
      <lat>29.708751</lat>
      <lon>-98.129226</lon>
      <ele>189.5</ele>
      <usgs>190.47114563</usgs>
    </waypoint>
    <waypoint id='3276'>
      <lat>29.708848</lat>
      <lon>-98.129246</lon>
      <ele>189.5</ele>
      <usgs>190.526168823</usgs>
    </waypoint>
    <waypoint id='3277'>
      <lat>29.708977</lat>
      <lon>-98.129241</lon>
      <ele>189.0</ele>
      <usgs>190.57901001</usgs>
    </waypoint>
    <waypoint id='3278'>
      <lat>29.709377</lat>
      <lon>-98.129271</lon>
      <ele>189.0</ele>
      <usgs>190.639160156</usgs>
    </waypoint>
    <waypoint id='3279'>
      <lat>29.709469</lat>
      <lon>-98.129293</lon>
      <ele>188.6</ele>
      <usgs>190.479202271</usgs>
    </waypoint>
    <waypoint id='3280'>
      <lat>29.709781</lat>
      <lon>-98.129473</lon>
      <ele>187.1</ele>
      <usgs>188.740097046</usgs>
    </waypoint>
    <waypoint id='3281'>
      <lat>29.70985</lat>
      <lon>-98.129516</lon>
      <ele>187.1</ele>
      <usgs>186.875045776</usgs>
    </waypoint>
    <waypoint id='3282'>
      <lat>29.710227</lat>
      <lon>-98.129579</lon>
      <ele>182.8</ele>
      <usgs>186.259033203</usgs>
    </waypoint>
    <waypoint id='3283'>
      <lat>29.710671</lat>
      <lon>-98.129506</lon>
      <ele>185.2</ele>
      <usgs>187.88911438</usgs>
    </waypoint>
    <waypoint id='3284'>
      <lat>29.710937</lat>
      <lon>-98.129505</lon>
      <ele>185.2</ele>
      <usgs>188.508087158</usgs>
    </waypoint>
    <waypoint id='3285'>
      <lat>29.711244</lat>
      <lon>-98.129508</lon>
      <ele>185.7</ele>
      <usgs>188.748046875</usgs>
    </waypoint>
    <waypoint id='3286'>
      <lat>29.711732</lat>
      <lon>-98.129516</lon>
      <ele>186.2</ele>
      <usgs>189.647216797</usgs>
    </waypoint>
    <waypoint id='3287'>
      <lat>29.712531</lat>
      <lon>-98.129541</lon>
      <ele>187.6</ele>
      <usgs>190.19859314</usgs>
    </waypoint>
    <waypoint id='3288'>
      <lat>29.712943</lat>
      <lon>-98.12959</lon>
      <ele>188.1</ele>
      <usgs>190.476074219</usgs>
    </waypoint>
    <waypoint id='3289'>
      <lat>29.713151</lat>
      <lon>-98.129708</lon>
      <ele>188.1</ele>
      <usgs>190.726425171</usgs>
    </waypoint>
    <waypoint id='3290'>
      <lat>29.713532</lat>
      <lon>-98.130135</lon>
      <ele>188.6</ele>
      <usgs>190.724655151</usgs>
    </waypoint>
    <waypoint id='3291'>
      <lat>29.713936</lat>
      <lon>-98.130613</lon>
      <ele>188.6</ele>
      <usgs>190.561264038</usgs>
    </waypoint>
    <waypoint id='3292'>
      <lat>29.714287</lat>
      <lon>-98.131028</lon>
      <ele>187.6</ele>
      <usgs>190.382156372</usgs>
    </waypoint>
    <waypoint id='3293'>
      <lat>29.714679</lat>
      <lon>-98.1315</lon>
      <ele>189.0</ele>
      <usgs>190.15222168</usgs>
    </waypoint>
    <waypoint id='3294'>
      <lat>29.714996</lat>
      <lon>-98.131877</lon>
      <ele>191.0</ele>
      <usgs>189.912139893</usgs>
    </waypoint>
    <waypoint id='3295'>
      <lat>29.715365</lat>
      <lon>-98.132324</lon>
      <ele>189.0</ele>
      <usgs>189.597198486</usgs>
    </waypoint>
    <waypoint id='3296'>
      <lat>29.715456</lat>
      <lon>-98.132445</lon>
      <ele>189.5</ele>
      <usgs>189.54876709</usgs>
    </waypoint>
  </segment>

  <turn id='88'>
    <fromto>Elizabeth Ave. to Edgewater Terrace</fromto>
    <cue>RIGHT onto Edgewater Terrace</cue>
    <comments>Edgewater Terrace T's in on the right.</comments>
  </turn>

  <segment id='88'>
    <road>Edgewater Terrace</road>
    <fromto>Elizabeth Ave. to Houston Ave.</fromto>
    <comments>The houses on the left are some of the coolest in New Braunfels.
      They have a private river behind them with trails around it.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3297'>
      <lat>29.715614</lat>
      <lon>-98.13248</lon>
      <ele>189.0</ele>
      <usgs>189.553405762</usgs>
    </waypoint>
    <waypoint id='3298'>
      <lat>29.715658</lat>
      <lon>-98.132451</lon>
      <ele>189.5</ele>
      <usgs>189.533172607</usgs>
    </waypoint>
    <waypoint id='3299'>
      <lat>29.716042</lat>
      <lon>-98.132043</lon>
      <ele>189.5</ele>
      <usgs>189.671875</usgs>
    </waypoint>
    <waypoint id='3300'>
      <lat>29.716442</lat>
      <lon>-98.131584</lon>
      <ele>189.5</ele>
      <usgs>189.684249878</usgs>
    </waypoint>
    <waypoint id='3301'>
      <lat>29.716814</lat>
      <lon>-98.131161</lon>
      <ele>191.4</ele>
      <usgs>189.558563232</usgs>
    </waypoint>
    <waypoint id='3302'>
      <lat>29.717162</lat>
      <lon>-98.130769</lon>
      <ele>190.0</ele>
      <usgs>189.5834198</usgs>
    </waypoint>
    <waypoint id='3303'>
      <lat>29.71746</lat>
      <lon>-98.130444</lon>
      <ele>190.0</ele>
      <usgs>189.6980896</usgs>
    </waypoint>
    <waypoint id='3304'>
      <lat>29.717622</lat>
      <lon>-98.130258</lon>
      <ele>189.5</ele>
      <usgs>189.71522522</usgs>
    </waypoint>
    <waypoint id='3305'>
      <lat>29.717936</lat>
      <lon>-98.12991</lon>
      <ele>189.0</ele>
      <usgs>189.804718018</usgs>
    </waypoint>
    <waypoint id='3306'>
      <lat>29.718241</lat>
      <lon>-98.129564</lon>
      <ele>189.5</ele>
      <usgs>190.223129272</usgs>
    </waypoint>
    <waypoint id='3307'>
      <lat>29.718588</lat>
      <lon>-98.129169</lon>
      <ele>191.0</ele>
      <usgs>191.267669678</usgs>
    </waypoint>
    <waypoint id='3308'>
      <lat>29.718979</lat>
      <lon>-98.128743</lon>
      <ele>191.0</ele>
      <usgs>192.251602173</usgs>
    </waypoint>
    <waypoint id='3309'>
      <lat>29.71932</lat>
      <lon>-98.128375</lon>
      <ele>190.5</ele>
      <usgs>192.516571045</usgs>
    </waypoint>
    <waypoint id='3310'>
      <lat>29.719461</lat>
      <lon>-98.128206</lon>
      <ele>190.5</ele>
      <usgs>192.535171509</usgs>
    </waypoint>
    <waypoint id='3311'>
      <lat>29.719671</lat>
      <lon>-98.127979</lon>
      <ele>190.0</ele>
      <usgs>192.523529053</usgs>
    </waypoint>
    <waypoint id='3312'>
      <lat>29.719988</lat>
      <lon>-98.127626</lon>
      <ele>190.5</ele>
      <usgs>192.394805908</usgs>
    </waypoint>
    <waypoint id='3313'>
      <lat>29.720056</lat>
      <lon>-98.127554</lon>
      <ele>190.5</ele>
      <usgs>192.339080811</usgs>
    </waypoint>
  </segment>

  <turn id='89'>
    <fromto>Edgewater Terrace to Houston Ave.</fromto>
    <cue>RIGHT onto Houston Ave.</cue>
    <comments>Edgewater Terrace dead-ends into Houston Ave.</comments>
  </turn>

  <segment id='89'>
    <road>Houston Ave.</road>
    <fromto>Edgewater Terrace to Austin St.</fromto>
    <comments>Pass through older neighborhoods.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3314'>
      <lat>29.720099</lat>
      <lon>-98.127382</lon>
      <ele>191.0</ele>
      <usgs>192.287918091</usgs>
    </waypoint>
    <waypoint id='3315'>
      <lat>29.720046</lat>
      <lon>-98.127294</lon>
      <ele>191.4</ele>
      <usgs>192.352096558</usgs>
    </waypoint>
    <waypoint id='3316'>
      <lat>29.719738</lat>
      <lon>-98.126906</lon>
      <ele>191.9</ele>
      <usgs>192.552597046</usgs>
    </waypoint>
    <waypoint id='3317'>
      <lat>29.719513</lat>
      <lon>-98.126641</lon>
      <ele>191.4</ele>
      <usgs>192.652603149</usgs>
    </waypoint>
    <waypoint id='3318'>
      <lat>29.719174</lat>
      <lon>-98.126252</lon>
      <ele>192.4</ele>
      <usgs>192.727645874</usgs>
    </waypoint>
    <waypoint id='3319'>
      <lat>29.718779</lat>
      <lon>-98.125797</lon>
      <ele>192.4</ele>
      <usgs>193.006973267</usgs>
    </waypoint>
    <waypoint id='3320'>
      <lat>29.718397</lat>
      <lon>-98.125338</lon>
      <ele>192.9</ele>
      <usgs>193.514968872</usgs>
    </waypoint>
    <waypoint id='3321'>
      <lat>29.718134</lat>
      <lon>-98.125024</lon>
      <ele>193.4</ele>
      <usgs>194.020584106</usgs>
    </waypoint>
    <waypoint id='3322'>
      <lat>29.717958</lat>
      <lon>-98.124809</lon>
      <ele>192.9</ele>
      <usgs>194.320770264</usgs>
    </waypoint>
    <waypoint id='3323'>
      <lat>29.717636</lat>
      <lon>-98.124414</lon>
      <ele>193.4</ele>
      <usgs>194.69241333</usgs>
    </waypoint>
    <waypoint id='3324'>
      <lat>29.717426</lat>
      <lon>-98.124158</lon>
      <ele>193.8</ele>
      <usgs>195.022216797</usgs>
    </waypoint>
    <waypoint id='3325'>
      <lat>29.717065</lat>
      <lon>-98.123745</lon>
      <ele>195.3</ele>
      <usgs>195.255554199</usgs>
    </waypoint>
    <waypoint id='3326'>
      <lat>29.716768</lat>
      <lon>-98.123392</lon>
      <ele>197.2</ele>
      <usgs>197.533096313</usgs>
    </waypoint>
    <waypoint id='3327'>
      <lat>29.716643</lat>
      <lon>-98.123215</lon>
      <ele>198.2</ele>
      <usgs>198.238616943</usgs>
    </waypoint>
  </segment>

  <turn id='90'>
    <fromto>Houston Ave. to Austin St.</fromto>
    <cue>LEFT onto Austin St.</cue>
    <comments>There's a hospital on the right corner.</comments>
  </turn>

  <segment id='90'>
    <road>Austin St.</road>
    <fromto>Houston Ave. to Central Ave.</fromto>
    <comments>One block connector.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3328'>
      <lat>29.71667</lat>
      <lon>-98.12304</lon>
      <ele>196.7</ele>
      <usgs>198.338363647</usgs>
    </waypoint>
    <waypoint id='3329'>
      <lat>29.716729</lat>
      <lon>-98.122954</lon>
      <ele>196.2</ele>
      <usgs>198.404067993</usgs>
    </waypoint>
    <waypoint id='3330'>
      <lat>29.717081</lat>
      <lon>-98.122558</lon>
      <ele>196.2</ele>
      <usgs>198.031616211</usgs>
    </waypoint>
    <waypoint id='3331'>
      <lat>29.717343</lat>
      <lon>-98.122282</lon>
      <ele>196.2</ele>
      <usgs>197.678604126</usgs>
    </waypoint>
    <waypoint id='3332'>
      <lat>29.717426</lat>
      <lon>-98.122188</lon>
      <ele>196.7</ele>
      <usgs>197.63079834</usgs>
    </waypoint>
  </segment>

  <turn id='91'>
    <fromto>Austin St. to Central Ave.</fromto>
    <cue>RIGHT onto Central Ave.</cue>
    <comments></comments>
  </turn>

  <segment id='91'>
    <road>Central Ave.</road>
    <fromto>Austin St. to Gruene Rd.</fromto>
    <comments>This is an older neighborhood.</comments>
    <lanes>1</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3333'>
      <lat>29.717476</lat>
      <lon>-98.122037</lon>
      <ele>196.2</ele>
      <usgs>197.672027588</usgs>
    </waypoint>
    <waypoint id='3334'>
      <lat>29.717426</lat>
      <lon>-98.121946</lon>
      <ele>196.7</ele>
      <usgs>197.672027588</usgs>
    </waypoint>
    <waypoint id='3335'>
      <lat>29.717361</lat>
      <lon>-98.121861</lon>
      <ele>197.7</ele>
      <usgs>197.761642456</usgs>
    </waypoint>
    <waypoint id='3336'>
      <lat>29.717097</lat>
      <lon>-98.121543</lon>
      <ele>197.7</ele>
      <usgs>198.195755005</usgs>
    </waypoint>
    <waypoint id='3337'>
      <lat>29.716773</lat>
      <lon>-98.121149</lon>
      <ele>198.6</ele>
      <usgs>198.653839111</usgs>
    </waypoint>
    <waypoint id='3338'>
      <lat>29.716516</lat>
      <lon>-98.120853</lon>
      <ele>198.6</ele>
      <usgs>198.977737427</usgs>
    </waypoint>
    <waypoint id='3339'>
      <lat>29.716191</lat>
      <lon>-98.120461</lon>
      <ele>199.1</ele>
      <usgs>199.131439209</usgs>
    </waypoint>
    <waypoint id='3340'>
      <lat>29.715815</lat>
      <lon>-98.120021</lon>
      <ele>198.6</ele>
      <usgs>199.035980225</usgs>
    </waypoint>
    <waypoint id='3341'>
      <lat>29.715701</lat>
      <lon>-98.119899</lon>
      <ele>198.6</ele>
      <usgs>199.031494141</usgs>
    </waypoint>
  </segment>

  <turn id='92'>
    <fromto>Central Ave. to Gruene Rd.</fromto>
    <cue>LEFT onto Gruene Rd.</cue>
    <comments>Gruene Rd. T's into Central Ave. on the left.</comments>
  </turn>

  <segment id='92'>
    <road>Gruene Rd.</road>
    <fromto>Central Ave. to Gruene Rd.</fromto>
    <comments>There is what looks like an estate on the right.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3342'>
      <lat>29.715687</lat>
      <lon>-98.119694</lon>
      <ele>198.2</ele>
      <usgs>199.070846558</usgs>
    </waypoint>
    <waypoint id='3343'>
      <lat>29.715717</lat>
      <lon>-98.119648</lon>
      <ele>197.7</ele>
      <usgs>199.070846558</usgs>
    </waypoint>
    <waypoint id='3344'>
      <lat>29.716007</lat>
      <lon>-98.119312</lon>
      <ele>198.6</ele>
      <usgs>199.325744629</usgs>
    </waypoint>
    <waypoint id='3345'>
      <lat>29.716329</lat>
      <lon>-98.118969</lon>
      <ele>198.6</ele>
      <usgs>199.373138428</usgs>
    </waypoint>
    <waypoint id='3346'>
      <lat>29.716669</lat>
      <lon>-98.11852</lon>
      <ele>197.2</ele>
      <usgs>195.697128296</usgs>
    </waypoint>
    <waypoint id='3347'>
      <lat>29.716925</lat>
      <lon>-98.11823</lon>
      <ele>194.3</ele>
      <usgs>191.137939453</usgs>
    </waypoint>
    <waypoint id='3348'>
      <lat>29.717352</lat>
      <lon>-98.117806</lon>
      <ele>191.9</ele>
      <usgs>189.039825439</usgs>
    </waypoint>
    <waypoint id='3349'>
      <lat>29.717437</lat>
      <lon>-98.117721</lon>
      <ele>191.9</ele>
      <usgs>189.090530396</usgs>
    </waypoint>
    <waypoint id='3350'>
      <lat>29.717824</lat>
      <lon>-98.117352</lon>
      <ele>191.4</ele>
      <usgs>189.403518677</usgs>
    </waypoint>
    <waypoint id='3351'>
      <lat>29.718193</lat>
      <lon>-98.117117</lon>
      <ele>191.0</ele>
      <usgs>189.684951782</usgs>
    </waypoint>
    <waypoint id='3352'>
      <lat>29.718584</lat>
      <lon>-98.116913</lon>
      <ele>192.4</ele>
      <usgs>189.666687012</usgs>
    </waypoint>
    <waypoint id='3353'>
      <lat>29.719168</lat>
      <lon>-98.116625</lon>
      <ele>192.4</ele>
      <usgs>189.47203064</usgs>
    </waypoint>
    <waypoint id='3354'>
      <lat>29.719822</lat>
      <lon>-98.116311</lon>
      <ele>192.4</ele>
      <usgs>189.32649231</usgs>
    </waypoint>
    <waypoint id='3355'>
      <lat>29.720336</lat>
      <lon>-98.116052</lon>
      <ele>192.4</ele>
      <usgs>189.26322937</usgs>
    </waypoint>
    <waypoint id='3356'>
      <lat>29.720859</lat>
      <lon>-98.115802</lon>
      <ele>190.5</ele>
      <usgs>189.2421875</usgs>
    </waypoint>
    <waypoint id='3357'>
      <lat>29.721392</lat>
      <lon>-98.115544</lon>
      <ele>190.5</ele>
      <usgs>189.242446899</usgs>
    </waypoint>
    <waypoint id='3358'>
      <lat>29.721672</lat>
      <lon>-98.115408</lon>
      <ele>189.5</ele>
      <usgs>189.246582031</usgs>
    </waypoint>
  </segment>

  <turn id='93'>
    <fromto>Gruene Rd. to Gruene Rd.</fromto>
    <cue>LEFT onto Gruene Rd.</cue>
    <comments>Gruene Rd. T's in on the left.  Gruene and Albert seem to merge
      here, which can be confusing, so keep your eye out for the Gruene
      Rd. sign on the left.</comments>
  </turn>

  <segment id='93'>
    <road>Gruene Rd.</road>
    <fromto>Gruene Rd. to parking</fromto>
    <comments>Go along the railroad tracks, under 46, across the river, and
      back up the hill into Gruene.</comments>
    <lanes>2</lanes>
    <shoulder>0</shoulder>
    <traffic>Light</traffic>
    <speed>30</speed>
    <waypoint id='3359'>
      <lat>29.721927</lat>
      <lon>-98.115402</lon>
      <ele>188.1</ele>
      <usgs>189.17074585</usgs>
    </waypoint>
    <waypoint id='3360'>
      <lat>29.722113</lat>
      <lon>-98.11555</lon>
      <ele>187.6</ele>
      <usgs>189.059524536</usgs>
    </waypoint>
    <waypoint id='3361'>
      <lat>29.722567</lat>
      <lon>-98.116083</lon>
      <ele>187.1</ele>
      <usgs>188.83416748</usgs>
    </waypoint>
    <waypoint id='3362'>
      <lat>29.722902</lat>
      <lon>-98.116465</lon>
      <ele>187.6</ele>
      <usgs>188.745574951</usgs>
    </waypoint>
    <waypoint id='3363'>
      <lat>29.72321</lat>
      <lon>-98.116797</lon>
      <ele>189.0</ele>
      <usgs>189.340377808</usgs>
    </waypoint>
    <waypoint id='3364'>
      <lat>29.723392</lat>
      <lon>-98.117007</lon>
      <ele>190.0</ele>
      <usgs>190.012664795</usgs>
    </waypoint>
    <waypoint id='3365'>
      <lat>29.723587</lat>
      <lon>-98.117235</lon>
      <ele>190.5</ele>
      <usgs>189.723358154</usgs>
    </waypoint>
    <waypoint id='3366'>
      <lat>29.723701</lat>
      <lon>-98.117364</lon>
      <ele>190.5</ele>
      <usgs>189.894668579</usgs>
    </waypoint>
    <waypoint id='3367'>
      <lat>29.723904</lat>
      <lon>-98.117567</lon>
      <ele>190.0</ele>
      <usgs>190.604888916</usgs>
    </waypoint>
    <waypoint id='3368'>
      <lat>29.724172</lat>
      <lon>-98.117843</lon>
      <ele>190.5</ele>
      <usgs>191.294494629</usgs>
    </waypoint>
    <waypoint id='3369'>
      <lat>29.724461</lat>
      <lon>-98.118146</lon>
      <ele>191.4</ele>
      <usgs>191.844070435</usgs>
    </waypoint>
    <waypoint id='3370'>
      <lat>29.724703</lat>
      <lon>-98.118423</lon>
      <ele>191.9</ele>
      <usgs>192.501739502</usgs>
    </waypoint>
    <waypoint id='3371'>
      <lat>29.725063</lat>
      <lon>-98.11882</lon>
      <ele>193.8</ele>
      <usgs>194.782165527</usgs>
    </waypoint>
    <waypoint id='3372'>
      <lat>29.725363</lat>
      <lon>-98.119125</lon>
      <ele>195.8</ele>
      <usgs>196.047363281</usgs>
    </waypoint>
    <waypoint id='3373'>
      <lat>29.72559</lat>
      <lon>-98.119174</lon>
      <ele>196.2</ele>
      <usgs>197.089096069</usgs>
    </waypoint>
    <waypoint id='3374'>
      <lat>29.725683</lat>
      <lon>-98.119134</lon>
      <ele>196.7</ele>
      <usgs>197.418807983</usgs>
    </waypoint>
    <waypoint id='3375'>
      <lat>29.726231</lat>
      <lon>-98.118815</lon>
      <ele>196.2</ele>
      <usgs>197.967544556</usgs>
    </waypoint>
    <waypoint id='3376'>
      <lat>29.726718</lat>
      <lon>-98.118523</lon>
      <ele>196.2</ele>
      <usgs>198.11869812</usgs>
    </waypoint>
    <waypoint id='3377'>
      <lat>29.727193</lat>
      <lon>-98.118243</lon>
      <ele>197.2</ele>
      <usgs>197.626190186</usgs>
    </waypoint>
    <waypoint id='3378'>
      <lat>29.727725</lat>
      <lon>-98.117928</lon>
      <ele>197.2</ele>
      <usgs>197.315200806</usgs>
    </waypoint>
    <waypoint id='3379'>
      <lat>29.728299</lat>
      <lon>-98.117584</lon>
      <ele>197.7</ele>
      <usgs>196.980239868</usgs>
    </waypoint>
    <waypoint id='3380'>
      <lat>29.728887</lat>
      <lon>-98.117235</lon>
      <ele>196.7</ele>
      <usgs>197.469100952</usgs>
    </waypoint>
    <waypoint id='3381'>
      <lat>29.729538</lat>
      <lon>-98.116863</lon>
      <ele>197.2</ele>
      <usgs>197.607223511</usgs>
    </waypoint>
    <waypoint id='3382'>
      <lat>29.730115</lat>
      <lon>-98.116538</lon>
      <ele>197.2</ele>
      <usgs>197.47442627</usgs>
    </waypoint>
    <waypoint id='3383'>
      <lat>29.730683</lat>
      <lon>-98.116212</lon>
      <ele>198.6</ele>
      <usgs>200.475463867</usgs>
    </waypoint>
    <waypoint id='3384'>
      <lat>29.731279</lat>
      <lon>-98.115904</lon>
      <ele>199.1</ele>
      <usgs>200.298431396</usgs>
    </waypoint>
    <waypoint id='3385'>
      <lat>29.731896</lat>
      <lon>-98.115593</lon>
      <ele>201.1</ele>
      <usgs>201.897079468</usgs>
    </waypoint>
    <waypoint id='3386'>
      <lat>29.732173</lat>
      <lon>-98.115388</lon>
      <ele>201.5</ele>
      <usgs>201.923919678</usgs>
    </waypoint>
    <waypoint id='3387'>
      <lat>29.732477</lat>
      <lon>-98.11503</lon>
      <ele>200.6</ele>
      <usgs>201.697494507</usgs>
    </waypoint>
    <waypoint id='3388'>
      <lat>29.732915</lat>
      <lon>-98.114487</lon>
      <ele>201.5</ele>
      <usgs>201.718643188</usgs>
    </waypoint>
    <waypoint id='3389'>
      <lat>29.7333</lat>
      <lon>-98.113991</lon>
      <ele>201.1</ele>
      <usgs>201.723587036</usgs>
    </waypoint>
    <waypoint id='3390'>
      <lat>29.733604</lat>
      <lon>-98.113515</lon>
      <ele>202.5</ele>
      <usgs>201.610488892</usgs>
    </waypoint>
    <waypoint id='3391'>
      <lat>29.733835</lat>
      <lon>-98.113053</lon>
      <ele>201.1</ele>
      <usgs>201.674316406</usgs>
    </waypoint>
    <waypoint id='3392'>
      <lat>29.73409</lat>
      <lon>-98.112376</lon>
      <ele>201.1</ele>
      <usgs>201.606246948</usgs>
    </waypoint>
    <waypoint id='3393'>
      <lat>29.734299</lat>
      <lon>-98.111986</lon>
      <ele>200.1</ele>
      <usgs>197.840362549</usgs>
    </waypoint>
    <waypoint id='3394'>
      <lat>29.734554</lat>
      <lon>-98.11158</lon>
      <ele>198.2</ele>
      <usgs>197.443710327</usgs>
    </waypoint>
    <waypoint id='3395'>
      <lat>29.734994</lat>
      <lon>-98.110876</lon>
      <ele>197.2</ele>
      <usgs>195.656555176</usgs>
    </waypoint>
    <waypoint id='3396'>
      <lat>29.73529</lat>
      <lon>-98.110422</lon>
      <ele>196.7</ele>
      <usgs>195.660980225</usgs>
    </waypoint>
    <waypoint id='3397'>
      <lat>29.735733</lat>
      <lon>-98.109721</lon>
      <ele>195.8</ele>
      <usgs>195.265335083</usgs>
    </waypoint>
    <waypoint id='3398'>
      <lat>29.736215</lat>
      <lon>-98.108974</lon>
      <ele>194.3</ele>
      <usgs>192.604095459</usgs>
    </waypoint>
    <waypoint id='3399'>
      <lat>29.736655</lat>
      <lon>-98.108277</lon>
      <ele>193.4</ele>
      <usgs>189.981506348</usgs>
    </waypoint>
    <waypoint id='3400'>
      <lat>29.736933</lat>
      <lon>-98.107832</lon>
      <ele>190.5</ele>
      <usgs>188.672592163</usgs>
    </waypoint>
    <waypoint id='3401'>
      <lat>29.736989</lat>
      <lon>-98.107741</lon>
      <ele>191.0</ele>
      <usgs>188.378585815</usgs>
    </waypoint>
    <waypoint id='3402'>
      <lat>29.737488</lat>
      <lon>-98.106948</lon>
      <ele>189.0</ele>
      <usgs>186.038406372</usgs>
    </waypoint>
    <waypoint id='3403'>
      <lat>29.737821</lat>
      <lon>-98.10646</lon>
      <ele>188.1</ele>
      <usgs>184.709594727</usgs>
    </waypoint>
    <waypoint id='3404'>
      <lat>29.738091</lat>
      <lon>-98.106259</lon>
      <ele>187.6</ele>
      <usgs>183.994308472</usgs>
    </waypoint>
    <waypoint id='3405'>
      <lat>29.738588</lat>
      <lon>-98.10601</lon>
      <ele>187.6</ele>
      <usgs>186.435516357</usgs>
    </waypoint>
    <waypoint id='3406'>
      <lat>29.738738</lat>
      <lon>-98.105871</lon>
      <ele>189.5</ele>
      <usgs>189.401412964</usgs>
    </waypoint>
    <waypoint id='3407'>
      <lat>29.738817</lat>
      <lon>-98.105758</lon>
      <ele>193.4</ele>
      <usgs>192.007278442</usgs>
    </waypoint>
    <waypoint id='3408'>
      <lat>29.738829</lat>
      <lon>-98.105737</lon>
      <ele>193.4</ele>
      <usgs>193.39831543</usgs>
    </waypoint>
    <waypoint id='3409'>
      <lat>29.738916</lat>
      <lon>-98.105549</lon>
      <ele>196.2</ele>
      <usgs>196.27571106</usgs>
    </waypoint>
    <waypoint id='3410'>
      <lat>29.738998</lat>
      <lon>-98.105371</lon>
      <ele>197.7</ele>
      <usgs>197.665756226</usgs>
    </waypoint>
    <waypoint id='3411'>
      <lat>29.739107</lat>
      <lon>-98.105131</lon>
      <ele>199.1</ele>
      <usgs>200.931396484</usgs>
    </waypoint>
    <waypoint id='3412'>
      <lat>29.739132</lat>
      <lon>-98.104926</lon>
      <ele>200.1</ele>
      <usgs>202.199508667</usgs>
    </waypoint>
    <waypoint id='3413'>
      <lat>29.7391</lat>
      <lon>-98.104827</lon>
      <ele>202.5</ele>
      <usgs>203.107727051</usgs>
    </waypoint>
    <waypoint id='3414'>
      <lat>29.739008</lat>
      <lon>-98.104713</lon>
      <ele>204.4</ele>
      <usgs>204.235992432</usgs>
    </waypoint>
    <waypoint id='3415'>
      <lat>29.738827</lat>
      <lon>-98.104563</lon>
      <ele>204.4</ele>
      <usgs>204.793273926</usgs>
    </waypoint>
    <waypoint id='3416'>
      <lat>29.738589</lat>
      <lon>-98.104376</lon>
      <ele>204.9</ele>
      <usgs>205.405334473</usgs>
    </waypoint>
    <waypoint id='3417'>
      <lat>29.7384</lat>
      <lon>-98.10421</lon>
      <ele>205.4</ele>
      <usgs>205.80581665</usgs>
    </waypoint>
    <waypoint id='3418'>
      <lat>29.738306</lat>
      <lon>-98.104043</lon>
      <ele>205.4</ele>
      <usgs>206.126815796</usgs>
    </waypoint>
  </segment>

  <!-- ******************************************* -->
  <!-- stops                                       -->
  <!-- ******************************************* -->

  <stop id='0a'>
    <type>conv. store</type>
    <description>There are many bars and restaurants in and surrounding
      Gruene.</description>
    <lat>29.738416</lat>
    <lon>-98.10415</lon>
  </stop>

  <stop id='0'>
    <type>conv. stores</type>
    <description>There are convenience stores at the corner of Hunter Rd. and
      FM 306.</description>
    <lat>29.744149</lat>
    <lon>-98.097777</lon>
  </stop>

  <stop id='1'>
    <type>truck stop</type>
    <description>There's a truck stop on the left at the corner of Conrads
      Ln. and I-35.</description>
    <lat>29.748665</lat>
    <lon>-98.059147</lon>
  </stop>

  <stop id='2'>
    <type>bar &amp; rest.</type>
    <description>Riley's is on the left just after you pass over the tracks.
      They claim to not open early; in fact, they claim to not even wake-up
      early.  Don't count on it for early morning rides.</description>
    <lat>29.805666</lat>
    <lon>-98.022674</lon>
  </stop>

  <stop id='3'>
    <type>conv. store</type>
    <description>There is a convenience store at the corner of River Rd. and
      Loop 337.</description>
    <lat>29.729346</lat>
    <lon>-98.125501</lon>
  </stop>

  <stop id='4'>
    <type>conv. store</type>
    <description>There is a convenience store at the corner of River Rd. and FM
      2673.</description>
    <lat>29.848415</lat>
    <lon>-98.174645</lon>
  </stop>

  <stop id='5'>
    <type>bar</type>
    <description>The River Rd. Icehouse is at the corner of River Rd.  and
      Hueco Springs Loop Rd.</description>
    <lat>29.747267</lat>
    <lon>-98.145209</lon>
  </stop>

  <stop id='6'>
    <type>stores</type>
    <description>There are several campgrounds and tubing companies with stores
      before you get to the first crossing. This is not an exact stop
      distance.</description>
    <lat>29.762472</lat>
    <lon>-98.140618</lon>
  </stop>

  <stop id='7'>
    <type>stores</type>
    <description>There are many campgrounds and tubing companies with stores
      between the first and second crossings. This is not an exact stop
      distance.</description>
    <lat>29.771681</lat>
    <lon>-98.158337</lon>
  </stop>

  <stop id='8'>
    <type>stores</type>
    <description>There are many campgrounds and tubing companies with stores
      between the second and third crossings. This is not an exact stop
      distance.</description>
    <lat>29.795614</lat>
    <lon>-98.150138</lon>
  </stop>

  <stop id='9'>
    <type>stores</type>
    <description>There are a few campgrounds and tubing companies with stores
      between the third and fourth crossings. This is not an exact stop
      distance.</description>
    <lat>29.822266</lat>
    <lon>-98.166435</lon>
  </stop>

  <stop id='10'>
    <type>conv. store</type>
    <description>There is a convenience store at the corner of Gruene Rd. and
      Common St.</description>
    <lat>29.722023</lat>
    <lon>-98.10069</lon>
  </stop>

  <stop id='11'>
    <type>conv. store</type>
    <description>There is a convenience store at the corner of Union Ave. and
      Common St.</description>
    <lat>29.709812</lat>
    <lon>-98.119746</lon>
  </stop>

  <!-- ******************************************* -->
  <!-- pois                                        -->
  <!-- ******************************************* -->

  <poi id='1'>
    <description>The local land-fill is on the right.</description>
    <lat>29.742733333</lat>
    <lon>-98.0301</lon>
  </poi>

  <poi id='2'>
    <description>First crossing.</description>
    <lat>29.765916667</lat>
    <lon>-98.141883333</lon>
  </poi>

  <poi id='3'>
    <description>Second crossing.</description>
    <lat>29.77895</lat>
    <lon>-98.159733333</lon>
  </poi>

  <poi id='4'>
    <description>Third crossing.</description>
    <lat>29.803733333</lat>
    <lon>-98.164083333</lon>
  </poi>

  <poi id='5'>
    <description>Fourth crossing.</description>
    <lat>29.84275</lat>
    <lon>-98.168066667</lon>
  </poi>

  <poi id='6'>
    <description>Start of old bridge.</description>
    <lat>29.697433333</lat>
    <lon>-98.106016667</lon>
  </poi>

  <poi id='7'>
    <description>End of old bridge.</description>
    <lat>29.697066667</lat>
    <lon>-98.1081</lon>
  </poi>

  <!-- ******************************************* -->
  <!-- Ridelist                                    -->
  <!-- ******************************************* -->

  <ride id='1'>
    <description>The short loop takes you out east of New Braunfels 
      into the countryside.</description>
    <parking_ref id='1' />
    <turn_ref id='1' />
    <segment_ref id='2' />
    <turn_ref id='2' />
    <segment_ref id='3' />
    <turn_ref id='3' />
    <segment_ref id='4' />
    <turn_ref id='4' />
    <segment_ref id='5' />
    <turn_ref id='5' />
    <segment_ref id='6' />
    <turn_ref id='6' />
    <segment_ref id='7' />
    <turn_ref id='7' />
    <segment_ref id='8' />
    <turn_ref id='8' />
    <segment_ref id='9' />
    <turn_ref id='10' />
    <segment_ref id='11' />
    <turn_ref id='11' />
    <segment_ref id='12' />
    <turn_ref id='12' />
    <segment_ref id='13' />
    <turn_ref id='13' />
    <segment_ref id='14' />
    <turn_ref id='14' />
    <segment_ref id='15' />
    <turn_ref id='15' />
    <segment_ref id='16' />
    <turn_ref id='16' />
    <segment_ref id='17' />
    <turn_ref id='16a' />
    <segment_ref id='17a' />
    <turn_ref id='17' />
    <segment_ref id='18' />
    <turn_ref id='18' />
    <segment_ref id='19' />
  </ride>

  <ride id='2'>
    <description>The medium route takes you through town and out and 
      back on River Rd.</description>
    <parking_ref id='1' />
    <turn_ref id='26' />
    <segment_ref id='26' />
    <turn_ref id='27' />
    <segment_ref id='27' />
    <turn_ref id='29' />
    <segment_ref id='29' />
    <turn_ref id='30' />
    <segment_ref id='30' />
    <turn_ref id='31' />
    <segment_ref id='31' />
    <turn_ref id='32' />
    <segment_ref id='32' />
    <turn_ref id='34' />
    <segment_ref id='34' />
    <turn_ref id='35' />
    <segment_ref id='35' />
    <turn_ref id='36' />
    <segment_ref id='36' />
    <turn_ref id='37' />
    <segment_ref id='37' />
    <turn_ref id='38' />
    <segment_ref id='38' />
    <turn_ref id='39' />
    <segment_ref id='39' />
    <turn_ref id='40' />
    <segment_ref id='40' />
    <turn_ref id='41' />
    <segment_ref id='41' />
    <turn_ref id='42' />
    <segment_ref id='42' />
  </ride>

  <ride id='3'>
    <description>The long route combines the short loop 
      and the medium route.</description>
    <parking_ref id='1' />
    <turn_ref id='1' />
    <segment_ref id='2' />
    <turn_ref id='2' />
    <segment_ref id='3' />
    <turn_ref id='3' />
    <segment_ref id='4' />
    <turn_ref id='4' />
    <segment_ref id='5' />
    <turn_ref id='5' />
    <segment_ref id='6' />
    <turn_ref id='6' />
    <segment_ref id='7' />
    <turn_ref id='7' />
    <segment_ref id='8' />
    <turn_ref id='8' />
    <segment_ref id='9' />
    <turn_ref id='10' />
    <segment_ref id='11' />
    <turn_ref id='11' />
    <segment_ref id='12' />
    <turn_ref id='12' />
    <segment_ref id='13' />
    <turn_ref id='13' />
    <segment_ref id='14' />
    <turn_ref id='14' />
    <segment_ref id='15' />
    <turn_ref id='15' />
    <segment_ref id='16' />
    <turn_ref id='16' />
    <segment_ref id='17' />
    <turn_ref id='16a' />
    <segment_ref id='17a' />
    <turn_ref id='17' />
    <segment_ref id='18' />
    <turn_ref id='50' />
    <segment_ref id='50' />
    <turn_ref id='27' />
    <segment_ref id='27' />
    <turn_ref id='29' />
    <segment_ref id='29' />
    <turn_ref id='30' />
    <segment_ref id='30' />
    <turn_ref id='31' />
    <segment_ref id='31' />
    <turn_ref id='32' />
    <segment_ref id='32' />
    <turn_ref id='34' />
    <segment_ref id='34' />
    <turn_ref id='35' />
    <segment_ref id='35' />
    <turn_ref id='36' />
    <segment_ref id='36' />
    <turn_ref id='37' />
    <segment_ref id='37' />
    <turn_ref id='38' />
    <segment_ref id='38' />
    <turn_ref id='39' />
    <segment_ref id='39' />
    <turn_ref id='40' />
    <segment_ref id='40' />
    <turn_ref id='41' />
    <segment_ref id='41' />
    <turn_ref id='42' />
    <segment_ref id='42' />
  </ride>

  <ride id='4'>
    <description>The shortest route is an urban option that is
      being considered as a route but hasn't been chose yet.</description>
    <parking_ref id='1' />
    <turn_ref id='76' />
    <segment_ref id='76' />
    <turn_ref id='77' />
    <segment_ref id='77' />
    <turn_ref id='78' />
    <segment_ref id='78' />
    <turn_ref id='79' />
    <segment_ref id='79' />
    <turn_ref id='80' />
    <segment_ref id='80' />
    <turn_ref id='80a' />
    <segment_ref id='80a' />
    <turn_ref id='81' />
    <segment_ref id='81' />
    <turn_ref id='82' />
    <segment_ref id='82' />
    <turn_ref id='83' />
    <segment_ref id='83' />
    <turn_ref id='84' />
    <segment_ref id='84' />
    <turn_ref id='85' />
    <segment_ref id='85' />
    <turn_ref id='86' />
    <segment_ref id='86' />
    <turn_ref id='87' />
    <segment_ref id='87' />
    <turn_ref id='88' />
    <segment_ref id='88' />
    <turn_ref id='89' />
    <segment_ref id='89' />
    <turn_ref id='90' />
    <segment_ref id='90' />
    <turn_ref id='91' />
    <segment_ref id='91' />
    <turn_ref id='92' />
    <segment_ref id='92' />
    <turn_ref id='93' />
    <segment_ref id='93' />
  </ride>

  <!-- ******************************************* -->
  <!-- History                                     -->
  <!-- ******************************************* -->

  <history>
    <update>
      <version>1</version>
      <date>2009-06-03</date>
      <description>Created short loop east of town.</description>
    </update>
    <update>
      <version>2</version>
      <date>2009-06-16</date>
      <description>Added medium distance ride on River Rd.</description>
    </update>
    <update>
      <version>3</version>
      <date>2009-06-16</date>
      <description>Added long distance ride and urban ride.</description>
    </update>
  </history>

</rideset>
"""
