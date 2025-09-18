# 8am AI!

August 27, 2025, 08:00 am

## Overview

- GitHub integration with the playground improves dynamic agent creation, as mentioned by David Olsson.
- Mercury platform demo showcased version two agent intelligence design system for outbound conversational agents with key components: persona creation, contact management, and conversation design.
- The demo created "Ava," a sales persona targeting organic leads via SMS campaign integration with High Level CRM.
- Advanced agent intelligence systems include batch operations and skills management, with evaluations running non-deterministic tests up to 4000 samples for confidence analytics.
- The system successfully executed 4000 OpenAI calls in 6 minutes through a serverless architecture, demonstrating efficiency.
- A CRM-agnostic design allows for easy integration across multiple platforms via RPC API, with Twilio as the SMS provider.
- Ethical concerns about AI disclosure were raised; research shows clients prefer non-disclosure regarding AI use in campaigns.
- The context management strategy involves workflow-based prompt systems to mitigate context rot during expanding conversations.
- User experience improvements suggest employing a meta-agent to assist with context engineering in client engagements.
- Tension exists between revealing system instructions and leveraging campaign learnings to optimize user experience in automated contexts.

## Notes

##### 🔍 **Opening & Context Setting** (00:00 - 02:21)
- David Olsson shared updates on GitHub repo integration with the playground for dynamic agent creation.
- Spencer MacBeth revealed he's working from Argentina, experiencing spring while others are in late summer.
- Discussion of weather conditions in Squamish with David explaining the 'foggus' phenomenon during August humidity.
##### 💻 **Mercury Platform Demo - Graham Fawcett** (05:11 - 14:40)
- Mercury introduced as version two agent intelligence conversation design system for outbound conversational agents.
- Platform features three core components: Persona creation, contact management, and conversation design.
- Demo showed creation of Ava, a sales representative persona with energetic tone, targeting organic leads with 20-minute AI assessment offer.
- Integration with High Level CRM demonstrated through automated workflow connecting Mercury APIs to SMS campaigns.
- Branching automation facilitates conversation loop between conversational context in Mercury and contact management in High Level.
- System waits several minutes to capture multiple contact responses before aggregating messages to Mercury.
- API supports dual purposes: first message generation and response message handling through single endpoint.
##### 🧠 **Agent Intelligence & Evaluation - Spencer MacBeth** (18:10 - 22:39)
- Demonstrated advanced deployment with batch operations, skills management, and evaluation systems.
- Skills defined as arbitrary capabilities like sentiment analysis, code generation, JSON parsing, and knowledge bases.
- Evaluation system runs non-deterministic tests at sample sizes up to 4000 with confidence levels using AWS Step Functions.
- Serverless infrastructure completed 4000 OpenAI calls in 6 minutes through distributed map execution.
- Monitoring system provides ongoing conversation analysis with hallucination detection, sentiment analysis, and custom alerts.
- Email alerting configured with thresholds for metrics like negative sentiment percentage or missing call-to-action links.
##### ⚙️ **Technical Architecture Discussion** (26:31 - 31:29)
- System designed to be CRM agnostic through RPC API supporting N8N, Make, and other platforms beyond High Level.
- External ID system enables workflows without upfront setup requirements.
- Full REST API available for technical users to create custom control planes within their applications.
- Twilio identified as underlying SMS provider through High Level's markup business model.
##### ⚖️ **Ethics & Disclosure Debate** (32:30 - 50:00)
- Jen Boger raised concerns about AI disclosure, questioning trust implications when bots don't reveal their nature.
- Graham Fawcett noted spectrum of user reactions, with personalized campaigns receiving better acceptance regardless of AI disclosure.
- Spencer MacBeth clarified that clients unanimously choose not to disclose AI nature, even when directly asked.
- Jason Kryski argued for strategic advantage by letting larger companies handle disclosure normalization while smaller companies optimize for competitive position.
- Fulvio Ciano emphasized lying as fundamental problem regardless of subject matter, citing negative billing precedent in Canadian telecom.
- David Olsson referenced historical examples of Angus Reed's dinner-time polling and Ted Rogers' negative billing as gray area innovations that later faced regulation.
##### 🔄 **Context Management & Technical Challenges** (53:33 - 55:51)
- Ashley Beckett inquired about context rot solutions in continuously expanding conversations.
- Spencer MacBeth explained workflow-based prompt systems with message types and global rules to minimize context degradation.
- Fulvio Ciano detailed standard summarization strategy at 60-70% context window threshold, converting negative to positive instructions.
- Graham Fawcett identified core challenge as determining exact context needed in agent's context window at execution time.
##### 👥 **User Experience & Onboarding** (59:34 - 01:02:41)
- Jen Boger suggested meta-agent for helping customers develop effective context engineering.
- Spencer MacBeth described current wizard-based approach helping clients identify objections, knowledge points, and scoped offers.
- Jason Kryski shared opposite approach using automated prompt chaining to generate context without user input, finding customers often don't know why people like their products.
- Graham Fawcett noted tension between surfacing system instructions versus built-in campaign learnings.

## Action items

##### **David Olsson**
- Hook up GitHub repos to the playground for direct repository analysis and dynamic agent creation (02:21)
##### **Spencer MacBeth**
- Share documentation links in chat and follow up with interested participants via email (22:39)
##### **Graham Fawcett**
- Consider implementing disclosure options and transparency features based on ethical feedback received (41:09)
- Evaluate onboarding agent concept for helping customers with context engineering (59:41)

