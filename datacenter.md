# DataCenter fa19-516-166

## E.Datacenter.2.b

There are two Google data centers in Council Bluffs, Iowa, the first of which opened in 2008, and the second announced in 2012.
Both data centers have roughly the same PUE (1.09 vs 1.11), though the following calculations are for the second one. In this area
of the country, the dollar per kWh is $.09. The IT workload of the center was not available online, but it was estimated to be
around 9000 kW based off of comparisons to other data centers. When all of this is put into the CO2 calculator hosted by Schneider
Electric, the annual electricity cost is $7.86 million and the total CO2 output is 77,429 tons (17070 equivalent in cars). 

One thing worth pointing out as well is Google's outreach to the
community in Council Bluffs since they built the data center there. The
Google page for the site mentions that Google has awarded $2 million to
local schools and nonprofits, as well as creating a free WiFi network
for everyone in the area. Of course these are probably part of some
agreement with the city and Google to benefit Google on breaks, its worth applauding Google for their efforts.

### Sources

* <https://www.google.com/about/datacenters/inside/locations/council-bluffs/>
* <https://www.google.com/about/datacenters/efficiency/internal/>
* <https://www.schneider-electric.com/en/work/solutions/system/s1/data-center-and-network-systems/trade-off-tools/data-center-carbon-footprint-comparison-calculator/>

## E.Datacenter.4

Solar power is the conversions of energy produced by the sun into
electricity through the use of solar panels.

The article provided in the book describes the massive solar farms that
Google is building in Alabama and Tennessee to power it's data centers
in those respective states. The two farms together will be composed of
1.6 million solar panels. Some other data centers that use solar power
are:

* Facebook's Henrico County data center in Virginia (under construction)
* Intel's New Mexico data center
* Apple's North Carolina and Nevada data centers
* Amazon also has six solar farms in Virginia to power its data centers
  
## E.Datacenter.5

AWS is currently in the process of transitioning to 100% renewable
energy to power its data centers by 2040. The sustainability section on
their website mentions that they achieved over 50% in 2018. Currently
they have six solar farms in Virginia, as well as wind farms in Indiana,
Ohio, and North Carolina. In April they announced plans to build three
more wind farms in California, Ireland, and Sweden. Additionally in
August they announced another wind farm for Ireland, and another solar
farm in Virginia. All of these projects are expected to be completed and
generating clean electricity by the end of 2020.

Amazon as a company has 53 active wind and solar projects across the
world now, and they have announced company-wide initiatives for net zero
carbon for all deliveries by the end of 2030. They are seen as a leader
in renewable energy by the Solar Industries Energy Association, having
the second most active solar panel installations (behind Apple).

Sources:

* <https://aws.amazon.com/about-aws/sustainability/>
* <https://www.businesswire.com/news/home/20190801005260/en/>
* <https://www.businesswire.com/news/home/20190408005471/en/Amazon-Announces-New-Renewable-Energy-Projects-Support>
* <https://www.cnbc.com/2019/08/02/amazon-announces-new-renewable-energy-projects-in-the-us-and-ireland.html>
  
## E.Datacenter.8

On February 28th 2017, the AWS data center in northern Virginia experienced a service disruption for roughly four hours during the
afternoon. It kind of broke the internet (both literally and figuratively). The outage affected S3 buckets for many
companies/services, including Slack, Venmo, Gizmodo, Apple Cloud, and many more. Some of these services were down completely,
while others just slowed down. It was later reported by Amazon that the outage was caused by an employee doing debugging
accidentally widened his scope too big and it dominoed the servers. 

As for the impact it had, obviously there were a large number of services that went down with the server. The Wall Street Journal
reported that the total outage cost S&P 500 companies $150 million dollars in lost revenue, as many retailers saw their website
performance drop. IU hosts all of its own services locally, but it just so happened that its Canvas instance was hosted on that
AWS server. So Canvas was down for roughly four hours, and it caused quite the increase in calls to UITS. Students were freaking
out they couldn't submit assignments, professors were complaining they couldn't administer quizzes/tests and so on. The graph
below shows number of users assisted by UITS that day. It's pretty clear to see just where the outage happened and how it effected
the university. The graph below was created using data from Indiana University University Information Technology Services, and the image was uploaded to imgur for simple hosting 

![AWS Outage [Source](https://www.npr.org/sections/thetwo-way/2017/03/03/518322734/amazon-and-the-150-million-typo)](https://i.imgur.com/1pB8nmn.png)

