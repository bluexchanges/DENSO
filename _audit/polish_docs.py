from pathlib import Path
import re
o=Path(__file__).parent.parent
pairs='''CFG 5|CFG5
K P I|KPI
V L M|VLM
A VS|AVS
RL DS|RLDS
N C|NC
trongrepo|trong repo
cellDENSO|cell DENSO
DigitalTwin|Digital Twin
digitaltwin|digital twin
costbasis|cost basis
netbenefit|net benefit
rubric2026|rubric 2026
DiffusionPolicy|Diffusion Policy
pretrainjoint|pretrain joint
painpoint|pain point
forcefeedback|force feedback
teachpendant|teach pendant
Teachpendant|Teach pendant
commandedTCP|commanded TCP
sampleefficiency|sample efficiency
accuracycao|accuracy cao
fullyloadedcost|fully loaded cost
basewage|base wage
costavoidance|cost avoidance
learnedjointsuccess|learned joint success
targetposterior|target posterior
engineeringrate|engineering rate
trongconfig|trong config
linklength|link length
jointzero|joint zero
Domainrandomization|Domain randomization
riskassessment|risk assessment
forcelimit|force limit
profilefixed|profile fixed
Nrollout|N rollout
trongsim|trong sim
tabRound1|tab Round 1
DENSO2025|DENSO 2025
doanhDENSO|doanh DENSO
materialhandling|material handling
FactoryAutomation|Factory Automation
Visualrepresentation|Visual representation
frozenencoder|frozen encoder
khaiDAgger|khai DAgger
actionsequence|action sequence
recedinghorizon|receding horizon
Generalistpolicy|Generalist policy
flowmatching|flow matching
actiongeneration|action generation
choPanda|cho Panda
researchrobot|research robot
haiinhand|hai in-hand
splitjoint|split joint
routequan|route quan
rubric2023|rubric 2023
pretrainablation|pretrain ablation
MCRcache|MCR cache
posteriorloss|posterior loss
jointtrain|joint train
Learnedjointrollout|Learned joint rollout
errorbaseline|error baseline
robotmodel|robot model
qualityhandshake|quality handshake
linkLinkedIn|link LinkedIn
trongtask|trong task
maskcamera|mask camera
outputjoint|output joint
taskcode|task code
sourceACT|source ACT
jointMCR|joint MCR
actionjoint|action joint
learnedpolicy|learned policy
tunejoint|tune joint
observationt|observation t
targetmeasuredq|target measured q
futuregrippercommand|future gripper command
measuredTCPstate|measured TCP state
CVAEposterior|CVAE posterior
multiviewmanifest|multiview manifest
Profileaccepted|Profile accepted
thaypose|thay pose
slotcode|slot code
bridgejoint|bridge joint
forcepolicy|force policy
featureB|feature B
trongconfigcontroller|trong config controller
forceprediction|force prediction
heldouttask|held-out task
engineeringeffort|engineering effort
trongNotes|trong Notes
marginaleffort|marginal effort
totalcost|total cost
IsaacLab|Isaac Lab
engineeringcost|engineering cost
headjoint|head joint
successflag|success flag
retargement|retargeting
cashflow|cash flow
calendarduration|calendar duration
Coreplan|Core plan
tasksuccess|task success
E25joint|E25 joint
tunejointxong|tune joint xong
productionwage|production wage
trongkhi|trong khi
priorinference|prior inference
fullyloadedlabor|fully loaded labor
implementationIsaacLab|implementation Isaac Lab
forcehead|force head
pretraindata|pretrain data
MCRpaper|MCR paper
theoquality|theo quality
Logcamera|Log camera
cachelogmaxfeatureerror|cache log max feature error
featureerror|feature error
capacitystudy|capacity study
jointpretrain|joint pretrain
freecommercial|free commercial
patchtheolog|patch theo log
rejectpath|reject path
ModelURDF|Model URDF
jointorder|joint order
actiondim|action dim
driverAPI|driver API
cellvalidation|cell validation
zerooffset|zero offset
toolframe|tool frame
trongchat|trong chat
Realimageheldout|Real image held-out
PandaMenagerie|Panda Menagerie
trackingerror|tracking error
frictiontrongMuJoCo|friction trong MuJoCo
khiinsert|khi insert
bufferage|buffer age
networkbandwidth|network bandwidth
Attentionmask|Attention mask
trackingcausalage|tracking causal age
contactevaluator|contact evaluator
independentvision|independent vision
codegenerator|code generator
safeenable|safe enable
dropflags|drop flags
Onlinewatchdog|Online watchdog
Cellstate|Cell state
qualityack|quality ack
goldenparttest|golden part test
operatorSOP|operator SOP
Checkpointcontracttrongtrain|Checkpoint contract trong train
Deploymentapproval|Deployment approval
lockedversion|locked version
heldoutregression|held-out regression
Thayrobot|Thay robot
accuracyACT|accuracy ACT
realrobot|real robot
cachejointMCRtheolog|cache joint MCR theo log
Observationt|Observation t
checkpointTCP|checkpoint TCP
policyjoint|policy joint
datasetpublic|dataset public
Tronginfoenv|Trong info env
offlinepositiondistance|offline position distance
qualitycheck|quality check
MCRpretrain|MCR pretrain
realdemo|real demo
learnedrolloutjoint|learned rollout joint
visualweights|visual weights
queryfrequency|query frequency
sinhreference|sinh reference
chungchung|chung chung
sungfeedback|sung feedback
integrationPLC|integration PLC
MESproduction|MES production
cellstate|cell state
Trongsim|Trong sim
saiembodiment|sai embodiment
safetygate|safety gate
sangbench|sang bench
shottrong|shot trong
taskpretrain|task pretrain
soACTrandom|so ACT random
chopretrain|cho pretrain
actionrepresentation|action representation
RecipeID|Recipe ID
subsetcamera|subset camera
cameraorder|camera order
haypreprocessing|hay preprocessing
historyE58TCP|history E58 TCP
priorbao|prior bao
coreplan|core plan
MCRweights|MCR weights
epochfrozen|epoch frozen
backboneforward|backbone forward
jointpolicy|joint policy
taskpilot|task pilot
modelrepresentation|model representation
visionbaseline|vision baseline
latentkhi|latent khi
temporalensembling|temporal ensembling
rolloutprotocol|rollout protocol
dataefficiency|data efficiency
actioncontract|action contract
taskscope|task scope
datafine|data fine
CVAEtrain|CVAE train
metricrobot|metric robot
labelproxy|label proxy
priorz0error|prior z=0 error
evalmode|eval mode
trainstats|train stats
cellsafety|cell safety
MCRfrozen|MCR frozen
ACTtrain|ACT train
jointexecutor|joint executor
Absoluteq|Absolute q
widthm|width m
Griddata|Grid data
logcache|log cache
Actionchunking|Action chunking
trainposterior|train posterior
inferencez|inference z
inferz|infer z
Imitationlearning|Imitation learning
actiondemo|action demo
baselinecell|baseline cell
executorjoint|executor joint
learnedjointrollout|learned joint rollout
developmentrollout|development rollout
failurereason|failure reason
gianepisode|gian episode
industrialproof|industrial proof
toolcalibration|tool calibration
problemcell|problem cell
labelcontroller|label controller
checkpointID|checkpoint ID
doRH20T|do RH20T
côngtyDMVN|công ty DMVN
tyDMVN|ty DMVN
vanVIC|van VIC
BTC2026|BTC 2026
RGB1280|RGB 1280
Round2|Round 2
LôE1|Lô E1
Report2025|Report 2025
ACT100|ACT 100
2inhand|2 in-hand
8Dnhư|8D như
head8D|head 8D
state8D|state 8D
trong00|trong 00
và0|và 0
1tỷ|1 tỷ
8h|8 h'''
mapping=dict(line.split('|',1) for line in pairs.splitlines())
pat=re.compile(r'(?<!\w)('+'|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True))+r')(?!\w)')
def polish(t):
 saved=[]
 def protect(m):saved.append(m[0]);return f'\x01{len(saved)-1}\x02'
 t=re.sub(r'```[\s\S]*?```|`[^`\n]+`|\[[^\]]*\]\(<[^>]+>\)|\[[^\]]*\]\(https?://[^\s]*?\)|https?://[^\s]+',protect,t)
 t=pat.sub(lambda m:mapping[m[1]],t)
 t=re.sub(r'([,;:])(?=[A-Za-zÀ-ỹ])',r'\1 ',t)
 t=t.replace('không đã đo','chưa phải số đo thực tế')
 return re.sub('\x01(\d+)\x02',lambda m:saved[int(m[1])],t)
for p in o.glob('*.md'):
 if int(p.name[:2])<4:continue
 p.write_text(polish(p.read_text(encoding='utf-8')),encoding='utf-8')
print('Polished 04-09; source links and inline code preserved.')
