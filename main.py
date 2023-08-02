import argparse
from extract_reference_features import getKidneyReferenceFeatures

parser = argparse.ArgumentParser()

parser.add_argument('--target', dest='target', default=None,type=str,
    help='directory with xml transformation targets')
parser.add_argument('--wsis', dest='wsis', default=None,type=str,
    help='directory of WSIs for reference feature extraction')
parser.add_argument('--chop_thumbnail_resolution', dest='chop_thumbnail_resolution', default=16,type=int,
    help='downsample mask to find usable regions')
parser.add_argument('--wsi_ext', dest='wsi_ext', default='.svs,.scn,.ndpi,.tif,.tiff' ,type=str,
    help='file ext of wsi images')
parser.add_argument('--min_size', dest='min_size', default=[30,30,24000,24000,10,10] ,type=int,
    help='min size region to be considered after prepass [in pixels]')

args = parser.parse_args()

getKidneyReferenceFeatures(args)
