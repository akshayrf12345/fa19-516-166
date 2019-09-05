# DataCenter

:o2: d not use the word "I"

## E.Datacenter.2.b

I decided to find information about the Google data center in Council Bluffs, Iowa. There are two Google data centers there, the first of which opened in 2008, and the second announced in 2012. I focused on the second data center, though the PUE is roughly the same for both of them (1.09 vs 1.11). In this area of the country, the dollar per kWh is $.09. I was not able to find the IT workload of the center, but I estimated it to be around 9000 kW based off of comparisons to other data centers. When all of this is put into the CO2 calculator hosted by Schneider Electric, the annual electricity cost is $7.86 million and the total CO2 output is 77,429 tons (17070 equivalent in cars). 


I decided to find information about the Google data center in Council
Bluffs, Iowa. There are two Google data centers there, the first of
which opened in 2008, and the second announced in 2012. I focused on the
second data center, though the PUE is roughly the same for both of them
(1.09 vs 1.11). In this area of the country, the dollar per kWh is $.09.
I was not able to find the IT workload of the center, but I estimated it
to be around 9000 kW based off of comparisons to other data centers.
When all of this is put into the CO2 calculator hosted by Schneider
Electric, the annual electricity cost is $7.86 million and the total CO2
output is 77,429 tons.


One thing I thought was interesting was Google's outreach to the
community in Council Bluffs since they built the data center there. The
Google page for the site mentions that Google has awarded $2 million to
local schools and nonprofits, as well as creating a free WiFi network
for everyone in the area. Of course these are probably part of some
agreement with the city and Google to benefit Google on breaks, but I
found it interesting nevertheless

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

On February 28th 2017, the AWS data center in northern Virginia experienced a service disruption for roughly four hours during the afternoon. It kinda of broke the internet (both literally and figuratively). The outage affected S3 buckets for many companies/services, including Slack, Venmo, Gizmodo, Apple Cloud, and many more. Some of these services were down completely, while others just slowed down. It was later reported by Amazon that the outage was caused by an employee doing debugging accidentally widened his scope too big and it dominoed the servers. 

As for the impact it had, obviously there were a large number of services that went down with the server. The Wall Street Journal reported that the total outage cost S&P 500 companies $150 million dollars in lost revenue, as many retailers saw their website performance drop. For me personally, I work with campus IT and was luckily enough to working at the time. While IU hosts all of its own services locally, it just so happened that our Canvas instance was hosted on that AWS server. So Canvas was down for roughly four hours, and I witnessed firsthand the chaos that it caused. We had students freaking out they couldn't submit assignments, professors complaining they could administer quizzes/tests and so on. The graph below shows number of customers we had during that day. It's pretty easy to look at that and see when we had the outage.

![AWS Outage [Source](https://www.npr.org/sections/thetwo-way/2017/03/03/518322734/amazon-and-the-150-million-typo)](https://i.imgur.com/1pB8nmn.png)

