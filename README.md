# Association rule-based discourse analysis (dis-rules)
The *dis-rules* project introduces association rule mining to discourse analysis. Compared to co-occurence approaches, the proposed approach advances the detection of clusters by reducing the bias towards highly frequent claims, thereby faciliating a better identification of discursive frames.

Parliamentary debates have been coded manually using the [Discourse Network Analyzer](https://github.com/leifeld/dna) developed by [Philip Leifeld](https://www.philipleifeld.com). The raw data has then been exported, cleaned and prepared for analysis in Python.

Datasets and Python code will be uploaded shortly.

The Python code allows us to:
* Use the popular [Apriori algorithm](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/) to:
    * Generate frequent itemsets
    * Find association rules
* Generate undirected network graphs from association rules
* Compute the [Louvain modularity score](https://github.com/taynaud/python-louvain/)

### Citation
If you use the dataset or code, please cite this paper:

Bhattacharya, Caroline (forthcoming), "Restrictive rules of speechmaking as a tool to maintain party unity: The case of oppressed political conflict in German parliament debates on the euro crisis", *Party Politics*, online first. doi: 10.1177/13540688221086226

For comments or questions, please contact the author: https://blogs.helsinki.fi/czwerner/
