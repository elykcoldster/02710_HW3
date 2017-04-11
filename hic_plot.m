clear;
load('hic_matrix.mat');

chr_res = 50000;
map_res = 100;

map = [ones(101,1) (1.0:-1.0/map_res:0)' (1.0:-1.0/map_res:0)'];

[xs,ys] = find(hic > 0);

imagesc(hic)
axis equal
axis([xs(1)-1 xs(end) ys(1)-1 ys(end)])
colormap(map)

title('Plot of TADs in given data');
xlabel('Chromosome Position');
ylabel('Chromosome Position');

xticks=[cellstr(num2str(get(gca,'xtick')'*chr_res))];
yticks=[cellstr(num2str(get(gca,'ytick')'*chr_res))];

set(gca, 'xticklabel', xticks);
set(gca, 'yticklabel', yticks);