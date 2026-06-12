##pangenomics

##GP:if you want to understand bioinformatic you have to read documentation properly not just running the command
##GP:any tools and packages you want to use first run followin command to find it usage
##bcz sometime documentation are old but packages and tools are updated so usage may be different 
tool_name -h
tool_name --help
##GP:you have to create environments by deactivating base to avoid conflicts with python versions

##conda install mamba through google
##first update conda base 
conda update -n base -c default conda
##you can use same commands as conda but write mamba instead of conda
##use pipelines panaroo,roary,anvi'o and install it through official page or github
##to Clean the Conda/Mamba cache and update mamba and conda
mamba clean --all
conda clean --all
conda update -n base -c defaults conda mamba
##to solve errors in conda/mamba make it prioority flexible instead of strict
conda config --set channel_priority strict
conda config --set channel_priority flexible
##to solve issue for using both mamba and conda in base
which mamba
unset MAMBA_ROOT_PREFIX
unset CONDA_ENVS_PATH
unset CONDA_PKGS_DIRS
unset MAMBA_ROOT_PREFIX
unset CONDA_ENVS_PATH
unset CONDA_PKGS_DIRS
nano ~/.bashrc
#export MAMBA_EXE='/home/mwu/miniconda3/bin/mamba';
#export MAMBA_ROOT_PREFIX='/home/mwu/.local/share/mamba';
##change above with following
export MAMBA_EXE='/home/mwu/miniconda3/bin/mamba';
export MAMBA_ROOT_PREFIX='/home/mwu/miniconda3'; 
##then ctrl+x then Y then Enter to save
##reload shell
source ~/.bashrc

#1- panaroo
https://github.com/gtonkinhill/panaroo?tab=readme-ov-file
https://gthlab.au/panaroo/#/gettingstarted/installation
##to verify all dependencies required or optional properly install or not run this command
python3 -c "import Bio, numpy, scipy, networkx, gffutils, edlib, joblib, tqdm; print('✅ All Python modules are present')"
for tool in cd-hit prokka prank mafft clustalw mash; do command -v $tool >/dev/null && echo "✅ $tool found" || echo "❌ $tool NOT found"; done
##download gff3 files through ncbi within a genus but different related species 
##or download within a species but different strains/individuals/organisms
##convert them into gff or alternatively use below method
##paste the fasta files in one same directory like /home/mwu/Documents/pangenomics_example/panaroo_example
##ls to verify all fasta files are present
##now run prokka for these fasta files bcz panaroo accept gff files
prokka file_name.fasta
prokka --outdir folder_name --prefix gff_file_name fasta_file_name.fa
##make folder for results inside the folder where gff files presents
mkdir results
panaroo -i *.gff -o results --clean-mode strict
##if you direct download gff3 file from ncbi refseq and convert it into gff manually then
##but if you run prokka it,s good bcz mostly it cannot recognize ncbi gff3 files
panaroo -i *.gff -o results --clean-mode strict --remove-invalid-genes
##clean-mode strict remove contamination including plasmids(i.e rare plasmids)
##because panaroo consider rare plasmid as contamination
##so if you want to keep plasmids then use clean-mode sensitive
panaroo -i *.gff -o results clean-mode sensitive
panaroo -i *.gff -o results1 --mode moderate
panaroo -i *.gff -o results2 --mode relaxed
##download cytoscape you get .sh file and to install .sh file use following commands
##bcz cytoscape need java 17 for function but open directory in which .sh file of cytoscape present
##or alternatively you give whole path /home/mwu/Downloads/Cytoscape_3_10_3_unix.sh
sudo apt update
sudo apt install openjdk-17-jdk
java -version
INSTALL4J_JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 ./Cytoscape_3_10_3_unix.sh
##to set JAVA_HOME globally (for future use) run following command
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
##use cytoscape to visualize graph
##https://manual.cytoscape.org/en/stable/
##click on import network button on top and navigate to path final_graph.gml file
##then download yfiles layout algorithms and select yfiles organic layout by clicking on top layout button
##you can differ between core and acessory gene by clicking on style button on side
##go to fill color and click mapping bar and select size in column and continous mapping in mapping type
##the genome size 1 mostly with light colors represent accessory genes while genome size 2 or greater than 2 as the number of genome you have in pangenome study mostly with dark colors represent core genes
##node= represent single gene or group/cluster of genes that make protein
##edge= represent line or link between two nodes
##network= represent collection of nodes and edges
##to see only accessory or core genes on the genome size click on filter button on side
##acessory genes have genome size 1 while core genes have genome size greater than 1
##select column filter then select node size according to which you want to analyze
##if you want to analyze accessory gene select node size between 1 and 1 inclusive so this show only acessory genes
##if you want to analyze core gene select node size between 1 and 3 inclusive or size between 1 and 2 inclusive or size between 3 and 3 inclusives or size between 3 and 3 inclusive this show only acessory genes





#2- anvio
##https://anvio.org/
##https://github.com/merenlab/anvio
##https://anvio.org/help/8/
##to fix error for installing anvi-setup-ncbi-cogs
anvi-setup-ncbi-cogs --cog-version COG20
cd $CONDA_PREFIX/lib/python3.10/site-packages/anvio/data/misc/COG/COG20/RAW_DATA_FROM_NCBI/
grep cog-20.cog.csv checksum.md5.txt
##1bed944a61e0ec404669361fb69ae52d  cog-20.cog.csv output
md5sum cog-20.cog.csv
##f38f319f5eccc9b9a81ffc7f4f933804  cog-20.cog.csv output
##both files output are different so that's why it give error now you fix it by running following command
##you can also check this by another alternative way
grep cog-20.cog.csv checksum.md5.txt > expected_checksum
md5sum cog-20.cog.csv > observed_checksum
diff expected_checksum observed_checksum
##if there is difference it will give output it mean you have to fix it 
##if it is same then it will not give output
##now you have to fix it
rm -rf cog-20.cog.csv
curl -O https://ftp.ncbi.nih.gov/pub/COG/COG2020/data/cog-20.cog.csv
md5sum cog-20.cog.csv
checksum.md5.txt cog-20.def.tab   fun-20.tab
##now do this for all files checksum.md5.txt, cog-20.def.tab, fun-20.tab, cog-20.cog.csv, cog-20.fa.gz
grep cog-20.fa.gz checksum.md5.txt
md5sum cog-20.fa.gz
##if both are same then no error if different then there is error and you have to fix it
##alternative way to check error
grep cog-20.fa.gz checksum.md5.txt > expected_checksum
md5sum cog-20.fa.gz > observed_checksum
diff expected_checksum observed_checksum
##now fix it
rm -rf cog-20.fa.gz
curl -O https://ftp.ncbi.nih.gov/pub/COG/COG2020/data/cog-20.fa.gz
md5sum cog-20.fa.gz
##After fixing them change directory and run
cd
anvi-setup-ncbi-cogs
anvi-setup-ncbi-cogs --cog-version COG20

##to solve issue related to pyani
pip install matplotlib==3.5.1

##https://merenlab.org/tutorials/vibrio-jasicida-pangenome/
##1- make folder of example_analysis
mkdir anvio_example1
##2- put your fasta files of refrence genome and strain genome of a specie in  a single folder
mkdir odoratimimus_genome
ls -l  
##to make sure that fasta files are present in directory
##3- rename your fasta file according to genome assembly like contig,scaffold,chromosome,complete e,g refrencegenome_complete.fasta or strain1_complete.fasta or strain31_complete.fasta
##4- then ls to verify that all files have same prefix like contig,scaffold,chromosome,complete
ls *fasta
##5- to convert fasta files into contig database which give .txt file bcz anvio used contigs-db
ls *fasta | awk 'BEGIN{FS="_"}{print $1}' > genomes.txt
##cat genomes.txt or less genomes.txt to check what is in .txt file
##6- Finalizing fasta files

for g in `cat genomes.txt`
do
    echo
    echo "Working on $g ..."
    echo
    anvi-script-reformat-fasta ${g}_complete.fasta \
                               --min-len 2500 \
                               --simplify-names \
                               -o ${g}_complete_2.5K.fasta
done
##if you donot want to remove nodes in your fasta file less than 2.5k nucleotides it mean the nodes that have only greater than 2500 nucleotides are remain other remove from above command you can set nucleotide as you wish
##7- Generating contig databases it give .db files

for g in `cat genomes.txt`
do
    echo
    echo "Working on $g ..."
    echo
    anvi-gen-contigs-database -f ${g}_complete_2.5K.fasta \
                              -o odoratimimus_${g}.db \
                              --num-threads 10 \
                              -n odoratimimus_${g}
done
##8- Annotating contigs databases to identify bacterial single-copy core genes, ribosomal RNAs, transfer RNAs among our contigs, and annotate our genes with functions 

for g in *.db
do
    anvi-run-hmms -c $g --num-threads 12
    anvi-run-ncbi-cogs -c $g --num-threads 12
    anvi-scan-trnas -c $g --num-threads 12
    anvi-run-scg-taxonomy -c $g --num-threads 12
done
##9- Taking a quick look at genome stats mean to check the simple features of these genomes that present in your contigs-db files
anvi-display-contigs-stats *db
##10- creating an external genome file to investigate contamination it check contigs-db files and make an external-genome.txt file
anvi-script-gen-genomes-file --input-dir . \
                             -o external-genomes.txt
##11- investigating contamination through external-genome.txt file
anvi-estimate-genome-completeness -e external-genomes.txt
##if in your genome list any genome have more redundancy or more num_splits or larger total lenght it means there is some contamination in that genome bcz when you apply --min-lens 2500 ther are still some nodes which are greater than 2500 nucleotides comes in your genome and create contamination so you have need to select that genome and refine it
##note from 12 to 17 commands are used to identify and remove contaminations if present
##12- visualizing contigs for refinement as for this we need profile database so --blank can generate a blank profile without any mapping results  
anvi-profile -c odoratimimus_strainPR63039.db \
             --sample-name odoratimimus_strainPR63039 \
             --output-dir odoratimimus_strainPR63039 \
             --blank
##13- as aresult a directory with AUXILIARY-DATA.db, PROFILE.db and RUNLOG.txt files created to use anvi-interactive which show us graph/display
anvi-interactive -c odoratimimus_strainPR63039.db \
                 -p odoratimimus_strainPR63039/PROFILE.db
##14- in phylogram or circle phylogram graph you can see if lenght is minimmum/low bar or intensity or line it mean it is contaminated so you can create bin as contamination or cleaned or odoratimimus_strainPR63039_cleaned or odoratimimus_strainPR63039_contaminated then click on store bin collection to save them as default you can also give any other name if you change name from default then you mention that change name instead of default in the -C default below command the method of save stat and load stat is also similiar as to store bin collection and load bin collection note its importan when you load stat or load bin collection click on draw button for visualization and displaying
anvi-split -p odoratimimus_strainPR63039/PROFILE.db \
           -c odoratimimus_strainPR63039.db \
           -C default \
           -o odoratimimus_strainPR63039_SPLIT
##so it give a directory of odoratimimus_strainPR63039_SPLIT which contain folders on the name of your bins that you created and in that folders CONTIGS.db file  is present 
##now we update the external-genome.txt file and create new external-genomes-final.txt file which is free of contamination and contain cleaned sequence as you done it through anvi-interactive and create bins of contaminated and clean
##15- now odoratimimus_strainPR63039_SPLIT/cleaned/CONTIGS.db is your working directory which you mention as path in command and you have no need to change directory be present in same directory where external-genome.txt file is present 
sed 's/odoratimimus_strainPR63039.db/odoratimimus_strainPR63039_SPLIT\/cleaned\/CONTIGS.db/g' external-genomes.txt > external-genomes-final.txt
##16- you can also compare the external-genomes.txt file and external-genomes-final.txt file by running following command
anvi-estimate-genome-completeness -e external-genomes.txt
anvi-estimate-genome-completeness -e external-genomes-final.txt
##17- computing the pangenome now you convert your external-genomes-final.txt file into odoratimimus-genomes.db which merges all the contigs databases .db files into a single, leaner contigs databases .db file
anvi-gen-genomes-storage -e external-genomes-final.txt \
                         -o odoratimimus-GENOMES.db
##18- if there is no contamination you can directly run it on external-genome.txt file to merges all the contigs databases .db files into a single, leaner contigs databases .db file
anvi-gen-genomes-storage -e external-genomes.txt \
                         -o odoratimimus-GENOMES.db
##19- now we ready to compute pangenome
anvi-pan-genome -g odoratimimus-GENOMES.db \
                --project-name Myroides_odoratimimus_pangenome_analysis \
                --num-threads 10
##it will create a folder basis on the --project-name Myroides_odoratimimus_pangenome_analysis and in that folder your .db file is present also on the name of --project-name Myroides_odoratimimus_pangenome_analysis-PAN.db and some other files but these two are important bcz you have to mention them in next as path in -p command
##20- displaying the pangenome which show phylogram or circle phylogram graph and give us interactive display
anvi-display-pan -p Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db \
                 -g odoratimimus-GENOMES.db
##change the background of refrence genome and redraw
##click on top layers button select gene_cluster frequencies tree then draw again
##click on top main button select all through edit attributes for multiple layers select height 0
##then click on top main button select the refrence genome and strain genomes you can do it through edit attributes for multiple layers and select height 180 for them
##click on top layers through edit attributes for multiple layers select height 0 and redraw
##21- to calculate average nucleotide identity(ANI)between each genome which tell us the the association/similarity between genomes
anvi-compute-genome-similarity --external-genomes external-genomes.txt \
                               --program pyANI \
                               --output-dir ANI \
                               --num-threads 10 \
                               --pan-db Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db
##if you want to use refine or contamination free file that you created after investigating contamination then use the updated external-genome-final.txt file
anvi-compute-genome-similarity --external-genomes external-genomes-final.txt \
                               --program pyANI \
                               --output-dir ANI \
                               --num-threads 10 \
                               --pan-db Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db
##23- Displaying ANI and adjusting it
anvi-display-pan -p Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db \
                 -g odoratimimus-GENOMES.db
##on layer tab in anvi-interactive or anvi-display unselect default and select ANI percentage identity and select min at 0.95 and which mean 95% mean genome which are 95% similiar or associated are highlighted when you click redraw layer data button 
##Inspecting amino acid sequence alignments you can click on genome it will give option of inspect gene cluster by clicking on it which will give amino acid sequence of gene
##Binning gene clusters when you create bin  by clicking on gene cluster number it will give detail of COG category, function & pathway
##Changing how gene clusters are ordered by clicking on top main button in display select item order as For instance, an ‘enforced synteny’ mean you order up gene cluster according to selected enforce synteny using the reference genome will change your display, where gene clusters will be ordered to respect the synteny of the genes they contain in the reference genome
##Selecting a range of gene clusters click at any point and select mark item as range start then add item range into active bin it will save in active bin
##Searching for functions it will search fuction in all region
##Searching using gene cluster filters it will search fuction in selected region as you wish highlight splits on tree and also append splits to selected bins from this the highlighted split is stored in bin and later you just visualize that part by storing bin
##Storing a collection you can store bin and load bin
##Splitting a pangenome to just visualize a specific region that you store in bin mean storing bin is only visualize
##24- to get detail information of store bin in terminal run following command
anvi-show-collections-and-bins -p Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db
##25- use splitting if you want a specific bin to visualize
anvi-split -p Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db \
           -g odoratimimus-GENOMES.db \
           --collection-name PR63039 \
           --bin-id PR63039 \
           --output-dir SPLIT
##it will create output directory of SPLIT and inside that on the basis of bin id another folder is created in which .db file is present which path you have to mention in next command to visualize that specificn split within major pangenome analysis
anvi-display-pan -p SPLIT/PR63039/PAN.db \
                 -g odoratimimus-GENOMES.db 
##if you want to delete a collection in which you store your bins first list the collection
anvi-delete-collection -p Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db --list-collections
##now delete which you want
anvi-delete-collection -p Myroides_odoratimimus_pangenome_analysis/Myroides_odoratimimus_pangenome_analysis-PAN.db -C unique_in_strain
##you can summarize pangenome by clicking on top bin button and click on generate a static summary page
##GC_###### is gene cluster id when you click on inspect gene cluster it will show amino acid sequence alignment of the genomes with their amino acid sequence id you can get this by bringing cursor and click on mouse feature which will also open by ctrl+M or simple say mousing on GC_###### directly clicking on get AA sequence which will give >genome-name_amino-acid-sequence_id
##by clicking on gene cluster bin it will give detail information along COG category, pathway & function in that it give specific COG acession COG#### by clicking on it you will get detailed information that gene cluster contain how genes which is equal to no of proteins and also show in how many organism this gene is present 
##The no of organisms and genes are different so do not confuse one organism may have the similiar gene multiple time 
##The anvio tool use word cluster refer to genomes that how many genomes you are using in your analysis if there is four genome and they aligned it mean that they are same that's why they aligned (alignment occur when different genome share the same gene OR each of the genomes contain one identical gene) so that specific GC id(gene of cluster)such as GC_####### have one similiar gene that present in four genomes 
##if any GC id GC_###### have two alignment mean one similiar genes present in two genomes and if it present in single genome it mean that it contain only gene that not present in any other genome so that,s why it not aligned with any other genome
##so cluster mean/represent all the genomes of different strain mean it's not cluster of gene it's different genomes cluster
##when you click on COG accession such as COG#### you enter in to another tab which contain its detail on links portion you find source:COG by clicking on it give a new detail page on that you see COG symbol:cas8b1 by this is your gene by clicking on it another tab of NCBI is open with it's detail information
##anvio can used both GCA Submitted GenBank assembly GCA_004337635.1 & NCBI RefSeq assembly GCF_004337635.1 so you can download fasta file of Genebank or Refseq according to your desired
##run pangenome explorer also it help you to find out gene detail easily otherwise you can also find gene and its detail without pangenome explore just through getting amino acid AA sequen and blast it which you get by clicking on Inspect gene cluster or by clicking on Get AA sequences. If there is gene in gene cluster ID GC_00003895 with COG ID COG1403 present on anvio you can find it through blast get the AA sequence of gene from anvio and blast protein you can find out your gene there by getting protein id under accession column as WP_058699415 the mostly 100% per.ident is your gene but compare the amino acid sequence as counter verification when you view it on ncbi click on identical protein groups you can find WP_058699415.1 is a RefSeq entry representing the protein across the Myroides genus (multispecies) and ALU26639.1 is a GenBank entry specific to Myroides odoratimimus strain. In source column it is written as RefSeq and INSDC check if your WP_058699415.1 refseq acession is similiar to some genebank ALU26639.1 insdc acession you can check it through position/range under CDS Region in Nucleotide column, organism column and strain column check if all are the same then it is your desired gene.
   



##https://merenlab.org/2016/11/08/pangenomics-v2/
##https://anvio.org/tutorials/pangenome-graphs/


#3- pan-genome explorer
##https://panexplorer.southgreen.fr/cgi-bin/home.cgi
##https://github.com/SouthGreenPlatform/PanExplorer
##open pan-genome explorer click on import genome and from ncbi check genebank id and put those which you want to analyze in pangenome analysis
##you can also see more detail of usage by clicking on doc button 
##make an yahoo account and login through email or login in your gmail account also into email bcz you have to enter email address not gmail otherwise it cannot processed
##note plz copy your URL link and save it somewhere to access it later when you wish bcz sometime email come but you cannot see it or sometime it maybe lost 
##URL: https://panexplorer.southgreen.fr/cgi-bin/panexplorer.cgi?uploadid=6693161421894.Myroides_odoratimimus
##URL: https://panexplorer.southgreen.fr/cgi-bin/panexplorer.cgi?uploadid=8699126677560.Vibrio_vulnificus_pangenome_analysis
##URL: https://panexplorer.southgreen.fr/cgi-bin/panexplorer.cgi?uploadid=2723862294546.stenotrophomonas_maltophila
##Term	             ##Example	        ##What It Means
Accession Number	ALU27791.1	      Unique ID for the protein in GenBank
Locus Tag	       AS202_17285	      Unique name for the gene in the genome
Position	      3833382..3835322	  Start and end nucleotide positions of the gene in genome
Protein             1..646	          Amino acid positions in the protein (total: 646 aa)
##The gene (with a locus tag, e.g., AS202_17285) is found at a specific position in the genome (e.g., 3833382..3835322).
##This gene is transcribed and translated to make a protein (with an accession number, e.g., ALU27791.1), which is a chain of amino acids (1..646).
##The protein accession number (ALU27791.1) is used to find the protein sequence in databases, while the locus tag is used to find the gene in the genome.
##Within one genome, multiple genes with the same COG may exist if they've duplicated over time.
##even in strain specific genes similiar COG exist in other dispensable genes or core genes
##COG numbers group genes that are evolutionarily related and often have similar functions.However, genes with the same COG number in different strains can be paralogs (gene copies that evolved new functions)or have slightly different roles in each strain, even if their general function is the same. 
##Paralogs are genes that arise by duplication they start out identical, then may evolve different functions or regulation.
##Sometimes, a strain-specific gene is a unique copy or variant (paralog) of a gene also found in other strains, but located elsewhere in the genome or with small sequence differences.The function (COG annotation) may be the same, but the gene’s actual sequence, location, or regulation can differ, making it unique to that strain.
##So Strain-specific genes are unique to one strain because of differences in their DNA sequence, position in the genome, or how they are turned on or off. Even if they have the same function (COG) as genes in other strains, they can still be different and only found in that one strain which make them strain specific genome/genes.
##pangenome explorer used GCA Submitted GenBank assembly GCA_004337635.1 which are annotated as well if it is not annotated it not submitted so check this before running pangenome but it also automatically remove them
##pangenome explorer give you protein id as a gene it's not actual gene or gene id and it give position you can find out its detail on ncbi by searching that protein id and find it in identical protein group you can check the sequence of protein/amino acid in it under protein column and also check sequence of DNA or RNA/nucleotide in it under CDS Region in Nucleotide column 
##you can also find locus tag in nucleotide or protein detail by after clicking on sequence of protein/amino acid in it under protein column and also check sequence of DNA or RNA/nucleotide in it under CDS Region in Nucleotide column 
##once you get locus tag now search it in gene database of ncbi bcz some time it is old locus tag so you get new locus tag and also get gene id from it and gene name which mention as gene symbol but always verify that range detail in gene ncbi database and position in pangenome explorer is same which show that you are looking for right gene
##if there is gene in gene cluster ID GC_00003895 with COG ID COG1403 present on anvio but not on pangenome explorer you can find it through blast get the AA sequence of gene from anvio and blast protein you can find out your gene there by getting protein id under accession column as WP_058699415 the mostly 100% per.ident is your gene but compare the amino acid sequence as counter verification when you view it on ncbi click on identical protein groups you can find WP_058699415.1 is a RefSeq entry representing the protein across the Myroides genus (multispecies) and ALU26639.1 is a GenBank entry specific to Myroides odoratimimus strain. In source column it is written as RefSeq and INSDC check if your WP_058699415.1 refseq acession is similiar to some genebank ALU26639.1 insdc acession you can check it through position/range under CDS Region in Nucleotide column, organism column and strain column check if all are the same then it is your desired gene.

 





#4- roary
https://sanger-pathogens.github.io/Roary/
https://github.com/sanger-pathogens/Roary
##first add channels then install roary by searching on google conda install roary but run through mamba command
##verify through conda/mamba list that your required packages and dependencies are installed
##if not installed install them through google by searching conda install dependency or package name
##ncbi-blast+ are separated install as blast and ncbi-vdb if not installed than install them through google conda install blast, ncbi-vdb etc
 

 












