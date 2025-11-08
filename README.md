[![build-test](https://github.com/darkwizard242/ansible-role-kubescape/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-kubescape/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-kubescape/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-kubescape/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/kubescape) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-kubescape&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-kubescape) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-kubescape&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-kubescape) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-kubescape?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-kubescape?color=orange&style=flat-square)

# Ansible Role: kubescape

Role to install (_by default_) `kubescape` on **Debian/Ubuntu** and **EL** systems. [kubescape](https://github.com/armosec/kubescape) is a K8s open-source tool providing a multi-cloud K8s single pane of glass, including risk analysis, security compliance, RBAC visualizer and image vulnerabilities scanning.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
kubescape_app: kubescape
kubescape_version: 3.0.44
kubescape_os: ubuntu
kubescape_dl_url: https://github.com/armosec/{{ kubescape_app }}/releases/download/v{{ kubescape_version }}/{{ kubescape_app }}-{{ kubescape_os }}-latest
kubescape_bin_path: "/usr/local/bin/{{ kubescape_app }}"
kubescape_file_owner: root
kubescape_file_group: root
kubescape_file_mode: '0755'
```

### Variables table:

Variable                      | Description
----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
kubescape_app                 | Defines the app to install i.e. **kubescape**
kubescape_version             | Defined to dynamically fetch the desired version to install. Defaults to: **3.0.44**
kubescape_os                  | Defines os type. Used for obtaining the correct type of binaries. Defaults to: **ubuntu**
kubescape_dl_url              | Defines URL to download the kubescape binary from.
kubescape_bin_path            | Defined to dynamically set the appropriate path to store kubescape binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin/kubescape**
kubescape_bin_permission_mode | Defines the permission mode level for the file.
kubescape_file_owner          | Owner for the binary file of kubescape.
kubescape_file_group          | Group for the binary file of kubescape.
kubescape_file_mode           | Mode for the binary file of kubescape.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **kubescape**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.kubescape
```

For customizing behavior of role (i.e. specifying the desired **kubescape** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.kubescape
  vars:
    kubescape_version: 2.0.155
```

For customizing behavior of role (i.e. placing binary of **kubescape** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.kubescape
  vars:
    kubescape_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-kubescape/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
