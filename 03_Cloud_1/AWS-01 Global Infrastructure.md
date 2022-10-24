# AWS-01 Global Infrastructure
A depth of understanding of the infra structure of AWS
#

## Key terminology
### Global Infrastructure

### IAM
#

## Exercise
Studying the infrastructure of AWS

### Sources
https://www.youtube.com/watch?v=0hlZvybbaGk

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio-explained.html

https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/

https://aws.amazon.com/cloudfront/features/?whats-new-cloudfront.sort-by=item.additionalFields.postDateTime&whats-new-cloudfront.sort-order=desc

https://www.techzine.nl/nieuws/cloud/458376/aws-breidt-cloudfront-tooling-uit-met-edge-functionaliteit/
#
### Overcome challenges
#
## Results
### What is an AWS availability zone (AZ)?
AWS AZ consists of one or more data centers. Multiple public and private subnets can be installed in it.

### What is a Region?
A region is a physical location somewhere in the world where there are multiple availability zones (AZs).

### What is an Edge Location?
An Edge location is an extension of the AZ. It brings the connection to the end user closer. This provides a faster connection and reduces latency.

### Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).
The choice also depends on the rules you have for each region, this is tied to what country the region is in and whether this matches the rules the end user complies with.

Waiting time is also an important factor. For faster trading, it is better to choose a region closer to the end user. This way there are fewer exchange points, reducing the waiting time.

The cost of using a region also varies by country. This, of course, can also play a role.

Services and features are generally the same with each region. Only the most new features and services are always adopted by the larger regions first, with smaller regions these are implemented later.

### Frankfurt or Oregon?
Depending on what the end user's requirements are, a choice can be made. If the end user is located in the Netherlands, the most obvious choice is Frankfurt. This is to reduce the waiting time and also for possible regulations.
