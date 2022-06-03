<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h2 align="center">DevOps Project G01</h2>

  <p align="center">
    A sentiment analysis project that has been implemented using Python, nltk and integrated with a CI/CD pipeline.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-using">Built Using</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#basic-workflow">Basic Workflow</a></li>
      </ul>
    </li>
    <li>
      <a href="#authors">Contributors</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a basic sentiment analysis project built for predicting the sentiment of restaurant reviews. It uses an SVM model that is built using Python's scikit-learn and nltk libraries. The model has been saved and stored in the Models folder inroot directory. A CI/CD pipeline has been built to integrate multiple DevOps project to create an end-to-end flow of the working, deployed application.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built Using

The following are the tools and technologies that have been used to complete this project - 
<div align="center">
  <img alt="DevOps Tools" src="https://github.com/AnaghaDAnanth/flask-cf-deployed/blob/main/images/image.png" width="700px" />
</div>

* [Slack Workstreams](https://workstreams.ai/slack.html?gclid=CjwKCAjwv-GUBhAzEiwASUMm4omTFkoEuciFBjWUa34t0q-d5ux3H1IfXyyaDZi6nqahWE37afFaTxoC6BQQAvD_BwE)
* [GitHub](https://github.com/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Cloud Foundry](https://www.cloudfoundry.org/)
* [BTP](https://www.sap.com/india/products/business-technology-platform.html)
* [Jenkins](https://www.jenkins.io/)
* [PyTest](https://docs.pytest.org/en/7.1.x/)
* [SonarQube](https://www.sonarqube.org/)
* [GitHub Actions](https://github.com/features/actions?utm_source=google&utm_medium=ppc&utm_campaign=2022q3-adv-WW-Google_Search-eg_brand&scid=7013o000002CdxYAAS&gclid=CjwKCAjwv-GUBhAzEiwASUMm4nXvdPw803qtqCPz7APeTtXLoWWSA29axZVQwtuNtvwG7Zbfa6jfxBoCBQ4QAvD_BwE)
* [NgRok](https://ngrok.com/)
* [GitHub WebHooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To run this project, make sure the public IP provided by ngrok is active. If so, trigger the Jenkins build by making a change in the repo.  

### Basic Workflow

Initially, a Jenkins pipeline is trigerred on changes being pushed to the repo. After the successful completion of the pipeline, new changes are pushed to the repo and GitHub actions triggers the deployment. A ‘main.yml’ file is defined, where scripts have been written to perform different jobs (Check, Deploy and Notify) for deployment.
  
<!-- AUTHORS -->
## Contributors
If you have a suggestion that would make this better, please fork the repo and create a pull request.
- Anagha D Ananth 
- Archana
- Natasha Sheelvant
- Neha Thipse 

<p align="right">(<a href="#top">back to top</a>)</p>
