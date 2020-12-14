# node2vec

This repository provides a reference implementation of *node2vec* as described in the paper:<br>
> node2vec: Scalable Feature Learning for Networks.<br>
> Aditya Grover and Jure Leskovec.<br>
> Knowledge Discovery and Data Mining, 2016.<br>
> <Insert paper link>

The *node2vec* algorithm learns continuous representations for nodes in any (un)directed, (un)weighted graph. Please check the [project page](https://snap.stanford.edu/node2vec/) for more details. 


### Installation

```
python -m pip install --upgrade git+https://github.com/ch3njust1n/node2vec
```

### Basic Usage

```
from node2vec import Graph


import argparse
import numpy as np
import networkx as nx
import node2vec
from gensim.models import Word2Vec


def parse_args():
	parser = argparse.ArgumentParser(description="Run node2vec.")

	...

	return parser.parse_args()


def read_graph():
	'''
	Reads the input network in networkx.
	'''
	...

	return G


def learn_embeddings(walks):
	'''
	Learn embeddings by optimizing the Skipgram objective using SGD.
	'''
	walks = [str(walk) for walk in walks]
	model = Word2Vec(walks, size=args.dimensions, window=args.window_size, min_count=0, sg=1, workers=args.workers, iter=args.iter)
	model.wv.save_word2vec_format(args.output)
	
	return


def main(args):
	'''
	Pipeline for representational learning for all nodes in a graph.
	'''
	nx_G = read_graph()
	G = node2vec.Graph(nx_G, args.directed, args.p, args.q)
	G.preprocess_transition_probs()
	walks = G.simulate_walks(args.num_walks, args.walk_length)
	learn_embeddings(walks)


if __name__ == "__main__":
	args = parse_args()
	main(args)
```

#### Input
The supported input format is an edgelist:

	node1_id_int node2_id_int <weight_float, optional>
		
The graph is assumed to be undirected and unweighted by default. These options can be changed by setting the appropriate flags.

#### Output
The output file has *n+1* lines for a graph with *n* vertices. 
The first line has the following format:

	num_of_nodes dim_of_representation

The next *n* lines are as follows:
	
	node_id dim1 dim2 ... dimd

where dim1, ... , dimd is the *d*-dimensional representation learned by *node2vec*.

### Citing
If you find *node2vec* useful for your research, please consider citing the following paper:

	@inproceedings{node2vec-kdd2016,
	author = {Grover, Aditya and Leskovec, Jure},
	 title = {node2vec: Scalable Feature Learning for Networks},
	 booktitle = {Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
	 year = {2016}
	}


### Miscellaneous

Please send any questions you might have about the code and/or the algorithm to <adityag@cs.stanford.edu>.

*Note:* This is only a reference implementation of the *node2vec* algorithm and could benefit from several performance enhancement schemes, some of which are discussed in the paper.
